from flask import Flask

app = Flask(__name__)


@app.route('/test', methods=['GET'])
def test():
    return 'this is a test'


app.run(port=8080)
