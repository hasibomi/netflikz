import datetime
from sqlalchemy.dialects.mysql import INTEGER

from netflikz.database import db


class VideoType(db.Model):
    id = db.Column(INTEGER(11, unsigned=True), primary_key=True, nullable=False)
    video_type = db.Column(db.String(50), nullable=False)
    videos = db.relationship('Video', backref='video_type', lazy=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now())


class Video(db.Model):
    id = db.Column(INTEGER(11, unsigned=True), primary_key=True, nullable=False)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    has_seasons = db.Column(db.Boolean, default=False, nullable=False)
    video_type_id = db.Column(INTEGER(11, unsigned=True), db.ForeignKey('video_type.id'))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now())
