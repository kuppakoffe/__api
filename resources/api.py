from flask_restful import Api
from services.Videos.Videos import Videos
from App.App import app


api = Api(app)
api.add_resource(Videos, "/video/<string:video_id>")