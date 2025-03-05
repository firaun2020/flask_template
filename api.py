from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def ping():
    data = request.get_json(silent=True) or {} 
    msg = data.get("msg")  

    if msg == "ping":
        return jsonify(response="Pong")
    if not data:  
        return jsonify(response="You forgot to say Hi")
    return jsonify(response="We not talking")

@app.route("/tellme", methods=["GET"])
def get_example():
    return "Security is overrated"


@app.route("/submit", methods=["GET"])
def get_example_workload():
    name = request.args.get("name", "Unknown")  
    return f"Technology sucks - Dr. {name}"


@app.route("/postbody", methods=["POST"])
def post_example_workload():
    data = request.get_json(silent=True) or {} 
    name = data.get("who")
    return f"WHo told you to be here Mr-{name}"



if __name__ == "__main__":
    app.run(debug=True)
