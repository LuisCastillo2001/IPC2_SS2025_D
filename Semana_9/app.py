from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Lista de productos en memoria
items = [
    {"id": 1, "name": "Manzana", "price": 1.2},
    {"id": 2, "name": "Banana", "price": 0.5}
]

# Mostrar archivo HTML con productos
@app.route("/")
def index():
    return render_template("index.html", items=items)

# GET → Listar productos
@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)

# POST → Agregar un producto
@app.route("/items", methods=["POST"])
def create_item():
    new_item = request.get_json()
    if len(items) == 0:
        new_item["id"] = 1
    else:
        new_item["id"] = items[-1]["id"] + 1
    items.append(new_item)
    return jsonify(new_item), 201

# PUT → Actualizar un producto completo
@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    updated_item = request.get_json()
    for item in items:
        if item["id"] == item_id:
            item["name"] = updated_item["name"]
            item["price"] = updated_item["price"]
            return jsonify(item)
    return jsonify({"error": "Producto no encontrado"}), 404

# PATCH → Actualizar parcialmente un producto
@app.route("/items/<int:item_id>", methods=["PATCH"])
def patch_item(item_id):
    patch_data = request.get_json()
    for item in items:
        if item["id"] == item_id:
            if "name" in patch_data:
                item["name"] = patch_data["name"]
            if "price" in patch_data:
                item["price"] = patch_data["price"]
            return jsonify(item)
    return jsonify({"error": "Producto no encontrado"}), 404

# DELETE → Eliminar un producto
@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    for i in range(len(items)):
        if items[i]["id"] == item_id:
            removed_item = items.pop(i)
            return jsonify({"message": f"Producto {removed_item['name']} eliminado"})
    return jsonify({"error": "Producto no encontrado"}), 404

if __name__ == "__main__":
    app.run(debug=True)
