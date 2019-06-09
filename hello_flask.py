from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_flask():
    return "Hello Flask!"

@app.route('/<name>')
def user(name):
    return "Hello " + name + "!"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='3333', debug=True)
