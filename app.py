from flask import Flask

app = Flask("hello")

@app.route("/")
@app.route("/hello")
def hello():
    return "Hello Word"

@app.route("/meucontato")
def meuContato():
    return """<html>
    <head>
        <title> Contatos </title>
    </head>
    <body>
     <a href="https://www.oceanbrasil.com/"> link para site da Ocean </a> 
    <h1>Villy von Rondow</h1>
    <h2>villyrondow@gmail.com</h2>
    </body>
    </html>"""