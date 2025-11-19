import flask
import requests

def check_status():
    """Fonction simple qui fait un appel HTTP pour illustrer l'usage des dépendances."""
    response = requests.get("https://httpbin.org/get")
    return response.status_code

app = flask.Flask(__name__)

@app.route("/")
def hello():
    status_code = check_status()
    return f"Hello, DevSecOps students! External status code = {status_code}"

if __name__ == "__main__":
    # Mode développement, suffisant pour le lab
    app.run(host="0.0.0.0", port=5000)
