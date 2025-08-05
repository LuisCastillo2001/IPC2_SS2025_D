import xml.etree.ElementTree as ET
from xml.dom import minidom
from xml.dom.minidom import Document


def menu_principal():
    ruta_reservaciones = ''
    while True:
        print('--------- MENU PRINCIPAL ---------')
        print('- 1. Cargar XML de reservaciones -')
        print('- 2. Leer reservaciones (minidom)-')
        print('- 3. Leer reservaciones (parse)  -')
        print('- 4. Escribir XML estudiantes (minidom) -')
        print('- 5. Escribir XML estudiantes (ET)      -')
        print('- 6. Salir                       -')
        print('----------------------------------')
        opcion = int(input('Seleccione una opción: '))
        match opcion:
            case 1:
                ruta_reservaciones = cargar_xml('reservaciones')
                if ruta_reservaciones == '':
                    print('Error: No se seleccionó un archivo')
                else:
                    print('Archivo de reservaciones cargado exitosamente')
                    print(ruta_reservaciones)
            case 2:
                leer_reservaciones_minidom(ruta_reservaciones)
            case 3:
                leer_reservaciones_parse(ruta_reservaciones)
            case 4:
                escribirConMiniDOM()
            case 5:
                escribirConET()
            case 6:
                print('Hasta luego')
                break
            case _:
                print('Opción no válida')

def cargar_xml(tipo):
    nombre_archivo = input(f"Ingrese el nombre del archivo XML de {tipo} (ejemplo: {tipo}.xml): ").strip()
    if nombre_archivo == '':
        return ''
    ruta_archivo = f'./entrada/{nombre_archivo}'
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            pass
        return ruta_archivo
    except FileNotFoundError:
        print(f'Archivo no encontrado: {ruta_archivo}')
        return ''

def leer_reservaciones_parse(ruta):
    if not ruta:
        print("Debe cargar primero el archivo de reservaciones.")
        return
    try:
        tree = ET.parse(ruta)
        root = tree.getroot()
        print(root.tag)
        if root.tag == 'reservaciones':
            for reservacion in root.findall('reservacion'):
                id = reservacion.get('id', '')
                descripcion = reservacion.find('descripcion').text 
                dia_elem = reservacion.find('dia')
                dia = dia_elem.text 
                hora = dia_elem.get('hora', '') 
                usuarios = []
                usuarios_elem = reservacion.find('usuarios')
                if usuarios_elem is not None:
                    for usuario in usuarios_elem.findall('usuario'):
                        usuario_id = usuario.get('id', '')
                        nombre = usuario.find('nombre').text if usuario.find('nombre') is not None else ''
                        carrera = usuario.find('carrera').text if usuario.find('carrera') is not None else ''
                        usuarios.append({'id': usuario_id, 'nombre': nombre, 'carrera': carrera})
                print('*'*40)
                print('ID:', id)
                print('Descripción:', descripcion)
                print('Día:', dia)
                print('Hora:', hora)
                print('Usuarios:')
                for u in usuarios:
                    print(f"  ID: {u['id']}, Nombre: {u['nombre']}, Carrera: {u['carrera']}")
        else:
            print("El archivo no contiene reservaciones.")
    except Exception as e:
        print(f"Error al leer reservaciones: {e}")

def leer_reservaciones_minidom(ruta):
    if not ruta:
        print("Debe cargar primero el archivo de reservaciones.")
        return
    try:
        dom = minidom.parse(ruta)
        root = dom.documentElement
        print(root.tagName)
        if root.tagName == 'reservaciones':
            reservaciones = root.getElementsByTagName('reservacion')
            print(f"Total de reservaciones: {len(reservaciones)}")
            for reservacion in reservaciones:
                id = reservacion.getAttribute('id')
                descripcion = reservacion.getElementsByTagName('descripcion')[0].firstChild.nodeValue
                dia_elem = reservacion.getElementsByTagName('dia')[0]
                dia = dia_elem.firstChild.nodeValue
                hora = reservacion.getElementsByTagName('dia')[0].getAttribute('hora')
                minutos = reservacion.getElementsByTagName('dia')[0].getAttribute('minutos')
                usuarios = []
                usuarios_elem = reservacion.getElementsByTagName('usuarios')[0]
                for usuario in usuarios_elem.getElementsByTagName('usuario'):
                    usuario_id = usuario.getAttribute('id')
                    nombre = usuario.getElementsByTagName('nombre')[0].firstChild.nodeValue
                    carrera = usuario.getElementsByTagName('carrera')[0].firstChild.nodeValue
                    usuarios.append({'id': usuario_id, 'nombre': nombre, 'carrera': carrera})
                print('*'*40)
                print('ID:', id)
                print('Descripción:', descripcion)
                print('Día:', dia)
                print('Hora:', hora)
                print('Minutos:', minutos)
                print('Usuarios:')
                for u in usuarios:
                    print(f"  ID: {u['id']}, Nombre: {u['nombre']}, Carrera: {u['carrera']}")
        else:
            print("El archivo no contiene reservaciones.")
    except Exception as e:
        print(f"Error al leer reservaciones: {e}")

def escribirConMiniDOM():
    doc = Document()
    root = doc.createElement('estudiantes')
    doc.appendChild(root)

    estudiantes = [
        {'carnet': '202400001', 'nombre': 'Estudiante 1', 'edad': '20'},
        {'carnet': '202400002', 'nombre': 'Estudiante 2', 'edad': '21'},
        {'carnet': '202400003', 'nombre': 'Estudiante 3', 'edad': '22'}
    ]

    for est in estudiantes:
        estudiante = doc.createElement('estudiante')
        estudiante.setAttribute('carnet', est['carnet'])
        root.appendChild(estudiante)

        nombre = doc.createElement('nombre')
        nombre.appendChild(doc.createTextNode(est['nombre']))
        estudiante.appendChild(nombre)

        edad = doc.createElement('edad')
        edad.appendChild(doc.createTextNode(est['edad']))
        estudiante.appendChild(edad)

    xml_str = doc.toprettyxml(indent='\t', encoding='utf-8')
    with open('salida/estudiantes.xml', 'wb') as archivo:
        archivo.write(xml_str)

def escribirConET():
    estudiantes = [
        {'carnet': '202400001', 'nombre': 'Estudiante 1', 'edad': '20'},
        {'carnet': '202400002', 'nombre': 'Estudiante 2', 'edad': '21'},
        {'carnet': '202400003', 'nombre': 'Estudiante 3', 'edad': '22'}
    ]
    root = ET.Element('estudiantes')
    for est in estudiantes:
        estudiante = ET.SubElement(root, 'estudiante')
        estudiante.set('carnet', est['carnet'])
        nombre = ET.SubElement(estudiante, 'nombre')
        nombre.text = est['nombre']
        edad = ET.SubElement(estudiante, 'edad')
        edad.text = est['edad']
    tree = ET.ElementTree(root)
    ET.indent(tree, space="\t", level=0)
    tree.write('salida/estudiantes_et.xml', encoding='utf-8', xml_declaration=True)

if __name__ == '__main__':
    menu_principal()