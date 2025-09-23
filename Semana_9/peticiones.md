# Peticiones para la API (curl)

Requisitos
- Ejecutar el servidor:
  python app.py
- Por defecto la API estará en: http://127.0.0.1:5000

Rutas disponibles (resumen)
- GET  /           → HTML (lista renderizada)
- GET  /items      → JSON (lista de productos)
- POST /items      → Crear producto
- PUT  /items/<id> → Reemplazar producto
- PATCH /items/<id>→ Actualizar parcialmente
- DELETE /items/<id>→ Eliminar producto

Ejemplos con curl

1) Obtener la página HTML (navegador o curl)
curl http://127.0.0.1:5000/

2) Listar todos los productos (JSON)
curl -s http://127.0.0.1:5000/items | jq .

3) Agregar un producto (POST)
Linux/macOS:
curl -X POST http://127.0.0.1:5000/items \
  -H "Content-Type: application/json" \
  -d '{"name":"Nuggets","price":3.5}'

Windows (PowerShell):
curl -X POST http://127.0.0.1:5000/items `
  -H "Content-Type: application/json" `
  -d '{"name":"Nuggets","price":3.5}'

Respuesta esperada: JSON del nuevo objeto y código 201

4) Reemplazar un producto (PUT)
Reemplaza completamente el producto con id 1:
curl -X PUT http://127.0.0.1:5000/items/1 \
  -H "Content-Type: application/json" \
  -d '{"name":"Manzana Roja","price":1.5}'

Respuesta esperada: JSON del producto actualizado o 404 si no existe

5) Actualizar parcialmente (PATCH)
Actualizar sólo el precio del producto id 2:
curl -X PATCH http://127.0.0.1:5000/items/2 \
  -H "Content-Type: application/json" \
  -d '{"price":0.7}'

6) Eliminar un producto (DELETE)
Eliminar producto id 2:
curl -X DELETE http://127.0.0.1:5000/items/2

Respuesta esperada: mensaje de confirmación o 404

Notas y consejos para estudiantes
- Comprobar respuestas y códigos HTTP (200, 201, 404).
- Si trabajas desde el navegador, la ruta `/` muestra la lista renderizada.
- La API en este ejemplo guarda datos en memoria: al reiniciar el servidor se pierden los cambios.
- Añadir validaciones en el servidor (por ejemplo, campos obligatorios y tipos) para prácticas adicionales.
