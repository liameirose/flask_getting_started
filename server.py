from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route("/name", methods=["GET"])
def name():
    name = {
         "name": "Lia Meirose"
    }
    return jsonify(name)


@app.route("/hello/<name>", methods=["GET"])
def hello(name):
    name = {
        "message": "Hello there,{}".format(name)
    }
    return jsonify(name)


@app.route("/distance", methods=["POST"])
def distance():
    r = request.get_json()
    dist = sqrt((r["b"][0]-r["a"][0])^2 + (r["b"][1]-r["a"][1])^2)
    final = {
        "distance": dist,
        "a": [r["a"][0],r["a"][1]],
        "b": [r["b"][0],r["b"][1]]
    }
    return jsonify(final)


if __name__ == "__main__":
    app.run(host="127.0.0.1")
