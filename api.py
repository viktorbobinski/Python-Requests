from flask_restful import Api, Resource
from flask import Flask

app = Flask(__name__)
api = Api(app)


names = {"tomek": {"age": 10, "gender": "male"},
         "kasia": {"age": 21, "gender": "female"}}


class HelloWorld(Resource):
    def get(self, name):
        return names[name]


api.add_resource(HelloWorld, "/hello_world/<string:name>")


if __name__ == '__main__':
    app.run(debug=True)