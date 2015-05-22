from recommender import db


class Recommend(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.String(300), nullable=False)

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __repr__(self):
        return 'Recommend: %r' % self.title
