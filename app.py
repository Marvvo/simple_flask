from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World! \nThis is a simple Flask application running in a Docker container.'

if __name__ == '__main__':
    app.run(debug=True)