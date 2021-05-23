from flask_restful import Resource


class HelloWorld(Resource):
    def get(self, name, age):
        return {"result": "Hello World, I am {} and i'm {} years old".format(name, age)}
    
    def post(self):
        return {"posted": True}