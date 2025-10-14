from flask import Flask, request, jsonify

app = Flask(__name__)

# Datos en memoria
alumnos = []
next_id = 1

@app.get('/alumnos')
def obtener_alumnos():
    # Método: GET
    # Body: ninguno
    # Respuesta: JSON con la lista de alumnos
    return jsonify(alumnos), 200

@app.post('/alumnos')
def crear_alumno():
    # Método: POST
    # Body (JSON) esperado: { "nombre": str, "correo": str, "cursos": [str, ...] }
    data = request.get_json(silent=True) or {}
    if not isinstance(data, dict):
        return jsonify({"error": "JSON inválido"}), 400

    nombre = data.get("nombre")
    correo = data.get("correo")
    cursos = data.get("cursos")

    if not nombre or not correo:
        return jsonify({"error": "Faltan campos: nombre y correo"}), 400

    if not isinstance(cursos, list) or not all(isinstance(c, str) for c in cursos):
        return jsonify({"error": "El campo 'cursos' debe ser una lista de strings"}), 400

    
    cursos_limpios = []
    for c in cursos:
        c_limpio = c.strip()
        if c_limpio:
            cursos_limpios.append(c_limpio)

    if not cursos_limpios:
        return jsonify({"error": "La lista 'cursos' no puede estar vacía"}), 400

    global next_id
    nuevo = {"id": next_id, "nombre": nombre, "correo": correo, "cursos": cursos_limpios}
    next_id += 1
    alumnos.append(nuevo)
    return jsonify(nuevo), 201

if __name__ == '__main__':
    app.run(debug=True)
