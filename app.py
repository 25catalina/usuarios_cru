from flask import Flask, render_template, request, redirect
from usuario import Usuario

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def registro():
    usuarios = Usuario.obtener_todos()
    print(usuarios)
    return render_template("crear_nuevo_usuario.html")

@app.route('/guardar', methods=["POST"])
def guardar():
    datos = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "gmail": request.form['gmail']}
    Usuario.guardar(datos)
    return redirect("/mostrar_usuario")


@app.route("/mostrar_usuario")
def mostrar_usuario():
    usuarios = Usuario.obtener_todos()
    return render_template("mostrar_usuario.html", usuarios=usuarios)

@app.route("/ver_usuario/<int:id>")
def ver_usuario(id):
    datos = {
        "id": id
    }
    usuario = Usuario.obtener_uno(datos)
    return render_template("ver_usuario.html", usuario=usuario)

@app.route("/borrar/<int:id>")
def borrar_usuario(id):
    datos = {
        "id": id
        }
    Usuario.eliminar(datos)
    return redirect("/mostrar_usuario")

@app.route("/editar/<int:id>")
def editar_usuario(id):
    datos = { "id": id }
    usuario = Usuario.obtener_uno(datos)
    return render_template("editar_usuario.html", usuario=usuario)

@app.route("/actualizar/<int:id>", methods=["POST"])
def actualizar_usuario(id):
    datos = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "gmail": request.form['gmail'],
        "id": id
    }
    Usuario.actualizar(datos)
    return redirect("/mostrar_usuario")

if __name__ == "__main__":
    app.run(debug=True)