from flask import Flask

app = Flask(__name__)

@app.get('/')
def herlenistalisson():
    return 'Valeu! Falou!'

@app.get('/pink')
def marilaquissandra():
    return 'mais uma vez'

@app.get('/frasedodia')
def backmelhorquefront():
    return 'Athos é muito lindo!'