from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def herlenistalisson():
    return render_template("index.html")


@app.get("/pink")
def marilaquissandra():
    return "mais uma vez"


@app.get("/nova")
def nova():
    return "nova"
