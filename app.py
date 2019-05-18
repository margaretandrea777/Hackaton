from flask import Flask, render_template
app=Flask(__name__)
@app.route("/")
def render_html():
    return render_template("bienvenida.html")

@app.route("/2da.html")
def render_index():
    return render_template("2da.html")

@app.route("/3ra.html")
def render_inde():
    return render_template("3ra.html")
