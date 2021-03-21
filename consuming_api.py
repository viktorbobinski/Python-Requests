from flask import Flask
from flask import jsonify
from flask import request
from flask import make_response

app = Flask(__name__)


@app.errorhandler(404)
def not_found(err):
    return make_response(jsonify({"error": "Not found"}), 404)


@app.route('/test_post', methods=['POST'])
def test_post():
    request_data = request.get_json()

    # return request_data, 201
    city = request.args.get('city')
    return jsonify(city=city), 201


@app.route('/test', methods=['GET'])
def test():
    return jsonify(result='this is a test'), 200


app.run(port=8080)
