python -m venv venv

### Para windows
venv\Scripts\activate

### Desactivar el entorno virtual
venv\Scripts\deactivate

### Instalar flask
pip install flask

### Estructura de carpetas
```
/mi_aplicacion
    /static
        /style.css
    /templates
        /index.html
        /about.html
        /lista.html
    app.py
```

### Expresiones jinja

- `{{ variable }}`: Para mostrar el valor de una variable.
- `{% for item in lista %} {% endfor %}`: Para iterar sobre una lista.
- `{% if condicion %} {% endif %}`: Para mostrar contenido condicionalmente.
