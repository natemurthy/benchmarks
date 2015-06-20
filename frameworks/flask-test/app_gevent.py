from gevent import pywsgi
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/api/rest/status",  methods=['GET'])
def get_status():
    response = {'DgmsInstanceId': 'dgms-service-0000'}
    return jsonify(response)

if __name__ == "__main__":
    app.debug = False
    addr = '0.0.0.0'
    port = 5000
    try:
        server = pywsgi.WSGIServer((addr, port), app)
        server.serve_forever()
    except KeyboardInterrupt:
        quit()
