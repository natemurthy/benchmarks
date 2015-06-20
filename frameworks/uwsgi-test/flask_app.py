from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/api/rest/status",  methods=['GET'])
def get_status():
    response = {'DgmsInstanceId': 'dgms-service-0000'}
    return jsonify(response)


