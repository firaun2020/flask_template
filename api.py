from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def ping():
    data = request.get_json()
    msg = data.get("msg")

    if msg =="ping":
        return jsonify(response="Pong")
    return jsonify(response="We not talking")


if __name__ == "__main__":
    app.run()