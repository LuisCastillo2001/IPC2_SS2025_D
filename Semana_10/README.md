# Proyecto: App de medicina (frontend Django + backend Flask)

Resumen
- Frontend: Django (paquete `medicine_app`) que consume el backend.
- Backend: Flask (endpoints en XML y JSON).
- Comunicación: soporta XML (/medicines) y JSON (/api/medicines).

---
## Contenido del repositorio
- backend/                -> Flask (app.py)
- frontend/medicine_app    -> Django (usar este paquete como único frontend)

---
## Requisitos generales
- Python 3.8+
- pip
- (opcional) virtualenv

---

## Backend (Flask) — ejecución rápida
1. Ir a `backend/`
2. Crear y activar entorno virtual:
   - Windows:
     - python -m venv venv
     - venv\Scripts\activate
   - Unix/macOS:
     - python -m venv venv
     - source venv/bin/activate
3. Instalar dependencias:
   - pip install -r requirements.txt
4. Ejecutar:
   - python app.py
5. Endpoints (resumen):
   - XML:
     - GET  /medicines
     - GET  /medicines/{id}
     - POST /medicines  (Content-Type: application/xml)
   - JSON:
     - GET  /api/medicines
     - GET  /api/medicines/{id}
     - POST /api/medicines (Content-Type: application/json)

Ejemplo curl XML (crear):
curl -i -X POST http://127.0.0.1:5000/medicines -H "Content-Type: application/xml" -d "<medicine><name>Ibuprofen</name><dose>200mg</dose><stock>50</stock></medicine>"

Ejemplo curl JSON (crear):
curl -i -X POST http://127.0.0.1:5000/api/medicines -H "Content-Type: application/json" -d '{"name":"Ibuprofen","dose":"200mg","stock":"50"}'

Notas:
- El backend usa almacenamiento en memoria (diccionario). Reiniciar la app borra los datos.
- Por defecto corre en http://127.0.0.1:5000

---

## Frontend (Django) — iniciar paso a paso
1. Ir a `frontend/`
2. Crear y activar entorno virtual:
   - python -m venv venv
   - Windows: venv\Scripts\activate
   - Unix/macOS: source venv/bin/activate
3. Instalar dependencias:
   - pip install -r requirements.txt
4. Ejecutar servidor de desarrollo:
   - python manage.py runserver
5. Abrir en el navegador:
   - http://127.0.0.1:8000/

La interfaz permite elegir formato (XML o JSON) y las acciones: Crear, Obtener por id, Listar.

---

## Explicación de los parámetros en settings.py
A continuación se explica cada opción que aparece en tu fragmento de settings:

- SECRET_KEY = 'replace-this-for-dev'
  - Clave secreta usada por Django para firmar cookies y tokens.
  - En desarrollo puede ser cualquier cadena; en producción debe ser secreta y fuerte.

- DEBUG = True
  - Modo de depuración. Muestra trazas y recarga automática.
  - Nunca activar en producción (riesgo de seguridad).

- ALLOWED_HOSTS = ['*']
  - Lista de hostnames permitidos para servir la app.
  - Para desarrollo `['*']` está bien, en producción poner dominios específicos.

- INSTALLED_APPS = [...]
  - Lista de aplicaciones Django activas. Aquí incluye `django.contrib.staticfiles` (para servir estáticos) y `medicine_app` (tu app).
  - Añade otras apps que uses (admin, auth, etc.) si las necesitas.

- MIDDLEWARE = [...]
  - Lista de middlewares que procesan peticiones/respuestas (ej. seguridad, sesiones).
  - `django.middleware.common.CommonMiddleware` aplica ajustes comunes como redirecciones de slash.

- ROOT_URLCONF = 'medicine_app.urls'
  - Módulo principal que define las rutas (urls) del proyecto.
  - Debe apuntar al archivo `urls.py` que registra las vistas.

- TEMPLATES = [...]
  - Configuración del motor de plantillas.
  - `DIRS` indica carpetas adicionales de plantillas; `APP_DIRS: True` permite que Django busque templates dentro de apps.

- WSGI_APPLICATION = 'medicine_app.wsgi.application'
  - Punto de entrada WSGI para servidores de producción (uWSGI, Gunicorn).
  - Para `runserver` no es estrictamente necesario, pero es requerido al desplegar.

- STATIC_URL = '/static/'
  - URL base para archivos estáticos (CSS, JS, imágenes).
  - En producción debes configurar `STATIC_ROOT` y ejecutar `collectstatic`.

---

## Consejos y buenas prácticas
- Ejecuta backend primero (puerto 5000), luego el frontend (8000).
- Usa un entorno virtual por proyecto.
- Para producción: desactivar DEBUG, asignar SECRET_KEY segura, configurar ALLOWED_HOSTS, usar base de datos persistente (no el dict en memoria) y servidor WSGI/ASGI apropiado.
- Si eliminas la carpeta `medicine_front` te quedas solo con `medicine_app` como fuente de configuración (para evitar confusión).

---

## Resumen rápido de comandos
- Backend:
  - cd backend
  - python -m venv venv
  - source venv/bin/activate  (o venv\Scripts\activate)
  - pip install -r requirements.txt
  - python app.py
- Frontend:
  - cd frontend
  - python -m venv venv
  - source venv/bin/activate  (o venv\Scripts\activate)
  - pip install -r requirements.txt
  - python manage.py runserver

---


