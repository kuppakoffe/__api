from flask_restful import Resource, reqparse, fields, marshal_with

from Services.Videos.Models.Videos import VideosModel

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

resource_fields = {
    'id': fields.Integer,
    "name": fields.String,
    "views": fields.Integer,
    "likes": fields.Integer
}


class Videos(Resource):

    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideosModel.query.get(id=video_id)
        return result

    def put(self, video_id):
        args = video_put_args.parse_args()
        videos[video_id] = args
        return {video_id: args}, 201
