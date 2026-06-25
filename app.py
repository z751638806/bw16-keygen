import os
import functools
from flask import Flask, request, Response, send_from_directory

app = Flask(__name__)

USERNAME = os.environ.get("AUTH_USER", "admin")
PASSWORD = os.environ.get("AUTH_PASS", "bw16keygen")


def check_auth(username, password):
    return username == USERNAME and password == PASSWORD


def authenticate():
    return Response(
        "需要身份验证",
        401,
        {"WWW-Authenticate": 'Basic realm="BW16 Keygen Login"'},
    )


def requires_auth(f):
    @functools.wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated


@app.route("/")
@requires_auth
def index():
    return send_from_directory(".", "activation_keygen.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
