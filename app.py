from flask import Flask
from gevent.pywsgi import WSGIServer


app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.cli.command("start")
def start():
    """ 帮助注释 """
    print("12133")


http_server = WSGIServer(("0.0.0.0", 8000), app)
http_server.serve_forever()

