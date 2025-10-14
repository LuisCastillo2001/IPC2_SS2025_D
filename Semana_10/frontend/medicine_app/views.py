from django.shortcuts import render
from django.http import HttpResponse
import requests
import xml.etree.ElementTree as ET

BACKEND_URL = 'http://127.0.0.1:5000'

def parse_medicines_xml(content):
    """Soporta tanto <medicines>... como una sola <medicine>."""
    try:
        root = ET.fromstring(content)
    except ET.ParseError:
        return None
    meds = []
    if root.tag == 'medicines':
        for m in root.findall('medicine'):
            med = {}
            for child in m:
                med[child.tag] = child.text
            meds.append(med)
    elif root.tag == 'medicine':
        med = {}
        for child in root:
            med[child.tag] = child.text
        meds.append(med)
    else:
       
        return None
    return meds

def parse_medicines_json(obj):
    """Normaliza respuesta JSON (dict o list) a lista de dicts con strings."""
    try:
        if isinstance(obj, list):
            return [{k: (str(v) if v is not None else '') for k, v in item.items()} for item in obj]
        elif isinstance(obj, dict):
            return [{k: (str(v) if v is not None else '') for k, v in obj.items()}]
    except Exception:
        return None
    return None

def index(request):
    """Carga la lista inicial desde el backend y renderiza la plantilla."""
    message = None
    medicines = []
    try:
        r = requests.get(f'{BACKEND_URL}/medicines', timeout=3)  # default XML list
        if r.status_code == 200:
            meds = parse_medicines_xml(r.content)
            if meds is not None:
                medicines = meds
            else:
                message = 'Error al parsear XML del backend.'
        else:
            message = f'Backend responded {r.status_code}'
    except requests.RequestException as e:
        message = f'Error contactando backend: {e}'
    return render(request, 'index.html', {'medicines': medicines, 'message': message})

def submit(request):
    """Procesa acciones create/get/list en XML o JSON según el campo 'format'."""
    if request.method != 'POST':
        return HttpResponse('Use POST', status=400)
    action = request.POST.get('action')
    fmt = request.POST.get('format', 'xml')  # 'xml' o 'json'
    name = request.POST.get('name', '')
    dose = request.POST.get('dose', '')
    stock = request.POST.get('stock', '')
    mid = request.POST.get('id', '').strip()

    # XML payload
    xml = f'<medicine><name>{name}</name><dose>{dose}</dose><stock>{stock}</stock></medicine>'
    headers_xml = {'Content-Type': 'application/xml'}
    message = None

    try:
        # -------------------------
        # XML flow
        # -------------------------
        if fmt == 'xml':
            if action == 'create':
                r = requests.post(f'{BACKEND_URL}/medicines', data=xml.encode('utf-8'), headers=headers_xml, timeout=3)
            elif action == 'get' and mid:
                r = requests.get(f'{BACKEND_URL}/medicines/{mid}', timeout=3)
            elif action == 'list':
                r = requests.get(f'{BACKEND_URL}/medicines', timeout=3)
            else:
                return HttpResponse('Acción inválida o falta id', status=400)

            if r.status_code in (200, 201):
                meds = parse_medicines_xml(r.content)
                if meds is not None:
                    # mostrar lista actualizada pidiendo la lista completa
                    rl = requests.get(f'{BACKEND_URL}/medicines', timeout=3)
                    medicines = parse_medicines_xml(rl.content) if rl.status_code == 200 else meds
                    message = 'Operación XML completada.'
                else:
                    medicines = []
                    message = 'La respuesta XML no es válida.'
            else:
                medicines = []
                message = f'Error del backend (XML): {r.status_code} {r.text}'

        # -------------------------
        # JSON flow
        # -------------------------
        else:
            if action == 'create':
                payload = {'name': name, 'dose': dose, 'stock': stock}
                r = requests.post(f'{BACKEND_URL}/api/medicines', json=payload, timeout=3)
            elif action == 'get' and mid:
                r = requests.get(f'{BACKEND_URL}/api/medicines/{mid}', timeout=3)
            elif action == 'list':
                r = requests.get(f'{BACKEND_URL}/api/medicines', timeout=3)
            else:
                return HttpResponse('Acción inválida o falta id', status=400)

            if r.status_code in (200, 201):
                try:
                    obj = r.json()
                    meds = parse_medicines_json(obj)
                    # pedir lista completa al backend para consistencia
                    rl = requests.get(f'{BACKEND_URL}/api/medicines', timeout=3)
                    medicines = parse_medicines_json(rl.json()) if rl.status_code == 200 else (meds or [])
                    message = 'Operación JSON completada.'
                except Exception:
                    medicines = []
                    message = 'La respuesta JSON no es válida.'
            else:
                medicines = []
                message = f'Error del backend (JSON): {r.status_code} {r.text}'

    except requests.exceptions.RequestException as e:
        return render(request, 'index.html', {'medicines': [], 'message': f'Error contacting backend: {e}'})

    return render(request, 'index.html', {'medicines': medicines, 'message': message})