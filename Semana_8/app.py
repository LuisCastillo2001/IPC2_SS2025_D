from flask import Flask, render_template, request, redirect, url_for
from linked_list import LinkedList


app = Flask(__name__)

#Inicializar la lista enlazada
tasks = LinkedList()

tasks.add("Realizar tarea de matemática")
tasks.add("Terminar práctica de IA")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        new_task = request.form.get("task")
        if new_task:
                tasks.add(new_task)
        return redirect(url_for("index"))
    
    return render_template("index.html", tasks = tasks)

@app.route("/tasks")
def show_tasks():
    return render_template("tasks.html", tasks= tasks)



@app.route("/toggle/<int:index>", methods=["POST"])
def toggle(index):
    tasks.toggle(index)
    return redirect(url_for("show_tasks"))

@app.route("/delete/<int:index>", methods=["POST"]) #localhost:5000/delete/:1
def delete(index):
    tasks.delete(index)
    return redirect(url_for("show_tasks"))

if __name__ == "__main__":
    app.run(debug=True)