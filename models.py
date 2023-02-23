
from setup_db import db

class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    trailer = db.Column(db.String)
    rating = db.Column(db.Float)
    year = db.Column(db.Integer)
    genre_id = db.Column(db.String, db.ForeignKey('genre.id'))
    genre = db.relationship('Genre')
    director_id = db.Column(db.String, db.ForeignKey('director.id'))
    director = db.relationship('Director')