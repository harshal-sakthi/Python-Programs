from flask import Flask

app = Flask(__name__)
@app.route('/')

def index():
    return "<h1>Hello This is my my First Flask App</h1>"

if __name__ == '__main__':
    app.run(debug=True)