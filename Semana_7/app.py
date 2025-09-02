from flask import Flask, render_template, request
import re

app = Flask(__name__)

# Diccionario de ejemplo
usuarios = {
    "luis": {"edad": 20, "pais": "Guatemala"},
    "ana": {"edad": 25, "pais": "El Salvador"},
    "carlos": {"edad": 30, "pais": "Honduras"}
}



# Expresión regular para validar nombre
nombre_regex = re.compile(r'^[A-Za-z]+$')

def validar_nombre(nombre):
    return bool(nombre_regex.match(nombre))

def leer_usuarios_archivo(filepath='data.txt'):
    usuarios_archivo = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for linea in f:
                partes = linea.strip().split(',')
                if len(partes) == 3:
                    usuarios_archivo.append((partes[0], partes[1], partes[2]))
    except FileNotFoundError:
        pass
    return usuarios_archivo

def agregar_usuario_archivo(nombre, edad, pais, filepath='data.txt'):
    try:
        with open(filepath, 'a', encoding='utf-8') as f:
            f.write(f"{nombre},{edad},{pais}\n")
        return True, "Usuario agregado correctamente."
    except Exception:
        return False, "Error al escribir en el archivo."

@app.route('/', methods=['GET', 'POST'])
def home():
    mensaje = ""
    datos_usuario = None
    mensaje_agregar = ""
    error_agregar = ""

    if request.method == 'POST':
        accion = request.form.get('accion', 'buscar')
        if accion == 'buscar':
            nombre = request.form.get('nombre', '').lower()
            if not validar_nombre(nombre):
                mensaje = "Nombre inválido, solo letras."
            elif nombre in usuarios:
                datos_usuario = usuarios[nombre]
            else:
                mensaje = "Usuario no encontrado."
        elif accion == 'agregar':
            nombre = request.form.get('nombre', '').strip()
            edad = request.form.get('edad', '').strip()
            pais = request.form.get('pais', '').strip()
            if not nombre or not edad or not pais:
                error_agregar = "Todos los campos son obligatorios."
            elif not validar_nombre(nombre):
                error_agregar = "Nombre inválido, solo letras."
            elif not edad.isdigit() or int(edad) < 0:
                error_agregar = "Edad inválida."
            else:
                exito, mensaje_archivo = agregar_usuario_archivo(nombre, edad, pais)
                if exito:
                    mensaje_agregar = mensaje_archivo
                else:
                    error_agregar = mensaje_archivo

    archivo_datos = leer_usuarios_archivo()

    return render_template(
        'index.html',
        mensaje=mensaje,
        datos_usuario=datos_usuario,
        archivo_datos=archivo_datos,
        mensaje_agregar=mensaje_agregar,
        error_agregar=error_agregar
    )

if __name__ == '__main__':
    app.run(debug=True)
      

