from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hola!</p>"

app.run(debug=True,port=5050)