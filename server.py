from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hola Mundo"

@app.route('/dojo')
def dojo():
    return "Dojo"

@app.route('/say/<string:name>')
def say(name):
    return f'Hello {name.capitalize()}'

@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    return f'{word}' * num

@app.errorhandler(404)
def page_not_found(e):
    return 'Lo siento, No hay respuesta. Intentalo otra vez.'

if __name__ == "__main__":
    app.run(debug = True)
