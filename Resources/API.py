from flask_restful import Api
from Services.Videos.VideoResource import VideoUnaryResource, VideosResource
from App.App import app

api = Api(app)
api.add_resource(VideoUnaryResource, "/api/video/<string:video_id>")
api.add_resource(VideosResource, "/api/videos")
