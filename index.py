from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# load data from JSON file
with open('users.json') as json_file:
    users = json.load(json_file)

@app.route('/login', methods=['POST'])
def login():
    # get username and password from request
    username = request.json['username']
    password = request.json['password']

    # check if username and password match
    if username in users and users[username] == password:
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "failed"})

if __name__ == '__main__':
    app.run()
