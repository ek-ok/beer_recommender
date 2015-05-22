from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from recommender.config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)

from recommender.views.rec import rec
from recommender.views.main import main
app.register_blueprint(rec, url_prefix='/recommend')
app.register_blueprint(main)