from flask import Flask, jsonify, request

app = Flask(__name__)

accounts = []

@app.route("/")
def home():
    return jsonify({"message": "Hello DevOps!"})

@app.route("/health")
def health_check():
    return jsonify({"status": "OK"}), 200

@app.route("/accounts", methods=["POST"])
def create_account():
    data = request.get_json()
    accounts.append(data)
    return jsonify(data), 201

@app.route("/accounts", methods=["GET"])
def get_accounts():
    return jsonify(accounts), 200

@app.route("/accounts/<int:index>", methods=["GET"])
def get_account(index):
    if index < len(accounts):
        return jsonify(accounts[index]), 200
    return {"error": "Not found"}, 404

@app.route("/accounts/<int:index>", methods=["PUT"])
def update_account(index):
    if index < len(accounts):
        data = request.get_json()
        accounts[index] = data
        return jsonify(data), 200
    return {"error": "Not found"}, 404

@app.route("/accounts/<int:index>", methods=["DELETE"])
def delete_account(index):
    if index < len(accounts):
        accounts.pop(index)
    return "", 204
