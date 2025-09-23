# Ejemplo Básico de API REST con Flask

## Enunciado del Ejemplo

Se desea crear una **API REST sencilla** utilizando Flask que permita gestionar una lista de productos. La API debe permitir:

1. **Listar productos** (`GET /items`)
2. **Agregar un producto** (`POST /items`)
3. **Actualizar un producto completo** (`PUT /items/<id>`)
4. **Actualizar parcialmente un producto** (`PATCH /items/<id>`)
5. **Eliminar un producto** (`DELETE /items/<id>`)
6. **Mostrar un archivo HTML** (`GET /`) con la lista de productos.

El objetivo es que los estudiantes practiquen los **conceptos básicos de Flask**, los **métodos HTTP** y cómo **renderizar HTML**.

---

## Conceptos importantes

### 1. Instalación de Flask
Se recomienda crear un entorno virtual:

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual (Windows)
venv\Scripts\activate

# Activar entorno virtual (Linux/Mac)
source venv/bin/activate

# Instalar Flask
pip install Flask

```

## Tabla de códigos de estado comunes

| Código | Nombre / Significado          | Cuándo usarlo |
|--------|-------------------------------|---------------|
| 200    | OK                            | La petición fue exitosa y devuelve datos (GET, PUT, PATCH). |
| 201    | Created                       | Recurso creado correctamente (POST). |
| 204    | No Content                    | La petición fue exitosa pero no hay contenido que devolver (DELETE). |
| 400    | Bad Request                   | La petición es inválida o faltan datos necesarios. |
| 401    | Unauthorized                  | No se ha autenticado o no tiene permisos. |
| 403    | Forbidden                     | La autenticación existe, pero no tiene permisos para ejecutar la acción. |
| 404    | Not Found                     | El recurso solicitado no existe (ej. item con id inexistente). |
| 405    | Method Not Allowed            | Se usa un método HTTP no permitido en ese endpoint (ej. POST en un GET). |
| 409    | Conflict                       | Conflicto en el estado del recurso (ej. id duplicado). |
| 500    | Internal Server Error          | Error del servidor, no relacionado con la petición del cliente. |

