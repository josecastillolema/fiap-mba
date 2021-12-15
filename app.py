from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1>Hola FIAP!</h1>\nMBA! v4 o/"

if __name__ == '__main__':
    # application.run()
    application.run(host='0.0.0.0', port=8080, debug=True)
