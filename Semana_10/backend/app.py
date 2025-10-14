from flask import Flask, request, Response, abort, jsonify
import xml.etree.ElementTree as ET

app = Flask(__name__)
db = {}
next_id = 1

def dict_to_xml(med):
    med_el = ET.Element('medicine')
    for k, v in med.items():
        el = ET.SubElement(med_el, k)
        el.text = str(v)
    return ET.tostring(med_el, encoding='utf-8')

def parse_medicine_xml(data):
    try:
        root = ET.fromstring(data)
        med = {}
        for child in root:
            med[child.tag] = child.text
        return med
    except ET.ParseError:
        return None

# -------------------------
# XML endpoints
# -------------------------
@app.route('/medicines', methods=['GET'])
def list_medicines():
    root = ET.Element('medicines')
    for mid, med in db.items():
        m = ET.SubElement(root, 'medicine')
        ET.SubElement(m, 'id').text = str(mid)
        for k, v in med.items():
            ET.SubElement(m, k).text = str(v)
    xml = ET.tostring(root, encoding='utf-8')
    return Response(xml, mimetype='application/xml')

#Ejemplo de peticion post
# curl -X POST -d '<medicine><name>Paracetamol</name><dose>500mg</dose><stock>100</stock></medicine>' -H "Content-Type: application/xml" http://

@app.route('/medicines/<int:mid>', methods=['GET'])
def get_medicine(mid):
    med = db.get(mid)
    if not med:
        abort(404)
    m = {'id': mid}
    m.update(med)
    return Response(dict_to_xml(m), mimetype='application/xml')

@app.route('/medicines', methods=['POST'])
def create_medicine():
    global next_id
    med = parse_medicine_xml(request.data)
    if med is None:
        return Response(b'Invalid XML', status=400)
    db[next_id] = med
    med_with_id = {'id': next_id}
    med_with_id.update(med)
    next_id += 1
    print(db)
    return Response(dict_to_xml(med_with_id), status=201, mimetype='application/xml')



# -------------------------
# JSON endpoints (/api)
# -------------------------
@app.route('/api/medicines', methods=['GET'])
def list_medicines_json():
    meds = []
    for mid, med in db.items():
        item = {'id': mid}
        item.update(med)
        meds.append(item)
    return jsonify(meds)

@app.route('/api/medicines/<int:mid>', methods=['GET'])
def get_medicine_json(mid):
    med = db.get(mid)
    if not med:
        return jsonify({'error': 'not found'}), 404
    item = {'id': mid}
    item.update(med)
    return jsonify(item)

@app.route('/api/medicines', methods=['POST'])
def create_medicine_json():
    global next_id
    data = request.get_json(silent=True)
    if not data or not isinstance(data, dict):
        return jsonify({'error': 'invalid json'}), 400
    # accept keys name,dose,stock
    med = {
        'name': data.get('name'),
        'dose': data.get('dose'),
        'stock': data.get('stock')
    }
    db[next_id] = med
    item = {'id': next_id}
    item.update(med)
    next_id += 1
    return jsonify(item), 201

if __name__ == '__main__':
    app.run(debug=True)
