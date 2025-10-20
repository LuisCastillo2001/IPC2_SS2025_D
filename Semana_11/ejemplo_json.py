import json
import xml.etree.ElementTree as ET

#Diccionario con diferentes tipos de datos JSON
diccionario_estudiante = {
    'id': 1,
    'nombre': 'Estudiante IPC',
    'edad': 18,
    'inscrito': True,
    'promedio': 70.5,
    'hobbies': ['lectura', 'programacion', 'musica'],
    'direccion': {
        'municipio': "Guatemala",
        'departamento': "Guatemala",
    }
}

#Convertir el diccionario a JSON
json_estudiante = json.dumps(diccionario_estudiante, indent=4)

#Sintaxis diccionario vs JSON
print('#---------- Sintaxis Diccionario ----------#')
print(diccionario_estudiante, '\n')
print('#---------- Sintaxis JSON ----------#')
print(json_estudiante, '\n')

#Convertir otros tipos de datos
print(json.dumps({'name': 'IPC2', 'age': 30}))
print(json.dumps(['Manzanas', 'Peras', 'Naranjas']))
print(json.dumps(['Manzanas', 123]))
print(json.dumps(('Manzanas', 'Naranjas', 'Naranjas')))
print(json.dumps('hola'))
print(json.dumps(30))
print(json.dumps(50.25))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


#########################################################################################################################################################
#########################################################################################################################################################

#Datos equivalentes en formato XML
xml_estudiante = """<?xml version="1.0" encoding="UTF-8"?>
<estudiante>
    <id>1</id>
    <nombre>Estudiante IPC</nombre>
    <edad>18</edad>
    <inscrito>true</inscrito>
    <promedio>70.5</promedio>
    <hobbies>
        <hobby>lectura</hobby>
        <hobby>programación</hobby>
        <hobby>musica</hobby>
    </hobbies>
    <direccion>
        <municipio>Guatemala</municipio>
        <departamento>Guatemala</departamento>
    </direccion>
</estudiante>"""

#Comparación tamaño de datos JSON vs XML
json_size = len(json_estudiante.encode('utf-8'))
print(f"\nTamaño de los datos JSON: {json_size} bytes")
xml_size = len(xml_estudiante.encode('utf-8'))
print(f"Tamaño de los datos XML: {xml_size} bytes")
print(f"JSON vs XML: JSON es {xml_size/json_size:.2f} veces más compacto que XML")

#########################################################################################################################################################
#########################################################################################################################################################

#Guardar JSON en un archivo .json
with open('estudiantes.json', 'w', encoding='UTF-8') as file:
    #json.dump serializa un objeto Python a formato JSON y lo escribe en un archivo
    #json.dumps genera una cadena JSON
    json.dump(diccionario_estudiante, file, indent=4, ensure_ascii=False)
print('JSON guardado en "estudiantes.json"')

#Leer el archivo JSON
with open('estudiantes.json',  'r', encoding='UTF-8') as file:
    #json.load parsea el contenido de un json a objeto de Python
    #json.loads 
    data = json.load(file) 
print('JSON leído correctamento y parseado a objeto Python')

#########################################################################################################################################################
#########################################################################################################################################################

xml_root = ET.fromstring(xml_estudiante)
print('Datos parseados desde XML')
print(f"Nombre: {xml_root.find('nombre').text}")
print(f"Primer hobby: {xml_root.find('hobbies/hobby').text}")

#Parsear JSON a diccionario
diccionario_json = json.loads(json_estudiante)
print('Datos parseados desde JSON')
print(f"Nombre: {diccionario_json['nombre']}")
print(f"Primer hobby: {diccionario_json['hobbies'][0]}")
