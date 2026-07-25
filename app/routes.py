from app import app
from flask import render_template, url_for

@app.route('/')
def home():
    return render_template("home.html")

@app.route("/contactos")
def contacto():
    return "Já na area dos Contacto"