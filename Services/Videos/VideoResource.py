import logging
from flask_restful import Resource, reqparse, fields, marshal_with

from Services.Videos.Models.Videos import VideoModel

from Tasks.tasks import celery

from Services.db import db

logger = logging.getLogger('video_resource')
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


class VideoUnaryResource(Resource):

    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()  # db.session.query(VideoModel).get(video_id)
        return result

    def delete(self, video_id):
        VideoModel.query.filter_by(id=video_id).delete()  # db.session.query(VideoModel).get(video_id)
        return True, 204

    # def put(self, video_id):
    #     args = video_put_args.parse_args()
    #     name = args['name']
    #     likes = args['likes']
    #     views = args['views']
    #     video = VideoModel(name=name, likes=likes, views=views)
    #     db.session.add(video)
    #     db.session.commit()


class VideosResource(Resource):

    def post(self):
        args = video_put_args.parse_args()
        name = args['name']
        likes = args['likes']
        views = args['views']
        video = VideoModel(name=name, likes=likes, views=views)
        # db.session.add(video)
        # db.session.commit()
        video_insert.delay(video)
        return {}

    @marshal_with(resource_fields)
    def get(self):
        return VideoModel.query.all()


@celery.task(name="celery.video_insert", serializer='json')
def video_insert(video: VideoModel):
    logger.info(video)
    db.session.add(video)
    db.session.commit()

