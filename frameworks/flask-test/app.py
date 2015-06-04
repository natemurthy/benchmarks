from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/api/rest/status",  methods=['GET'])
def get_status():
    response = dict()
    response['DgmsInstanceId'] = 'dgms-service-0000'
    return jsonify(response)

if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0', debug=True)
    except KeyboardInterrupt:
        logging.info("Shutting down server.")
        quit()
