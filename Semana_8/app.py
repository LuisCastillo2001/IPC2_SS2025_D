from flask import Flask, render_template, request, redirect, url_for
from linked_list import LinkedList

app = Flask(__name__)

# Inicializamos lista enlazada
tasks = LinkedList()
tasks.add("Estudiar Flask")
tasks.add("Terminar práctica de SO")
tasks.add("Revisar correos")
tasks.add("Hacer ejercicio")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        new_task = request.form.get("task")
        if new_task:
            tasks.add(new_task)
        return redirect(url_for("index"))

    return render_template("index.html", tasks=tasks)

@app.route("/tasks")
def show_tasks():
    return render_template("tasks.html", tasks=tasks)

@app.route("/delete/<int:index>", methods=["POST"])
def delete(index):
    current = tasks.head
    prev = None
    count = 0
    while current:
        if count == index:
            if prev:
                prev.next = current.next
            else:
                tasks.head = current.next
            break
        prev = current
        current = current.next
        count += 1
    return redirect(url_for("show_tasks"))

@app.route("/toggle/<int:index>", methods=["POST"])
def toggle(index):
    tasks.toggle(index)
    return redirect(url_for("show_tasks"))

if __name__ == "__main__":
    app.run(debug=True)
