from flask_restful import Resource, reqparse, HTTPException
from Exceptions.Exceptions import api_exceptions

videos = {}
video_put_args = reqparse.RequestParser()
video_put_args.add_argument(
    "name", type=str, help="name of the video", required=True
)
video_put_args.add_argument(
    "likes",
    type=int,
    help="number of likes on the video is required",
    required=True,
)
video_put_args.add_argument(
    "views", type=int, help="number of views on video", required=True
)


class VideosExceptions(HTTPException):
    pass


class Videos(Resource):
    def get(self, video_id):
        if video_id not in videos:
            return api_exceptions[404]
        return videos[video_id]

    def put(self, video_id):
        args = video_put_args.parse_args()
        videos[video_id] = args
        return {video_id: args}, 201
