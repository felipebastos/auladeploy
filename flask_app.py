from flask import Flask, render_template

import auth

app = Flask(__name__)

app.register_blueprint(auth.bp)


@app.get("/")
def herlenistalisson():
    return render_template("index.html")


@app.get("/pink")
def marilaquissandra():
    return "mais uma vez"


@app.get("/maisum")
def nova():
    return "Forcei a barra"
