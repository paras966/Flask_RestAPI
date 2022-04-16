from flask import Flask
from flask_restful import Api, Resource, reqparse, abort


app = Flask(__name__)
api= Api(app)

parser = reqparse.RequestParser()
parser.add_argument("name", type=str, help='name should be given', required=True)
parser.add_argument("likes", type=int, help='likes should be given', required=True)
parser.add_argument("views", type=int, help='views should be given', required=True)

videos = {}
def if_video_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404,message="Video not found...")

def if_video_exist(video_id):
    if video_id in videos:
        abort(409,message="Video Exist...")

class Video(Resource):
    def get(self,video_id):
        if_video_doesnt_exist(video_id)
        return videos[video_id]

    def put(self,video_id):
        if_video_exist(video_id)
        args = parser.parse_args()
        videos[video_id] = args
        return videos[video_id],201

    def delete(self, video_id):
        if_video_doesnt_exist(video_id)
        del videos[video_id]
        return "", 204

api.add_resource(Video, "/video/<string:video_id>")

if __name__=="__main__":
    app.run(debug=True)