from flask import Flask, render_template
app=Flask(__name__)
@app.route("/")
def render_html():
    return render_template("index.html")
