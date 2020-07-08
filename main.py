from flask import Flask, render_template   

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/lucas")
def lucas():
    return render_template("lucas.html")
    

@app.route("/compras")
def compras():
    return render_template("compras.html")

@app.route("/configuracion")
def configuracion():
    return render_template("configuracion.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/productos")
def productos():
    return render_template("productos.html")

@app.route("/marcelo")
def marcelo():
    return render_template("marcelo.html")

@app.route("/hora")
def hora():
    return render_template("hora.html")

@app.route("/brian")
def brian():
    return render_template("brian.html")


@app.route("/tabla")
def tabla():
    return render_template("tabla.html")

@app.route("/sebastian")
def sebastian():
    return render_template("sebastian.html")

@app.route("/gaspar")
def gaspar():
    return render_template("gaspar.html")
    
if __name__ == "__main__":    app.run(debug=True)