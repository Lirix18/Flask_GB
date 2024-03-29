from flask import Flask, render_template
from blog.views.users import users_app
from blog.views.articles import articles_app
from blog.views.authors import authors_app
from blog.models.database import db
from blog.views.auth import login_manager, auth_app
from blog.security import flask_bcrypt
from blog.admin import admin
import os
from flask_migrate import Migrate

from blog.api import init_api


cfg_name = os.environ.get("CONFIG_NAME") or "DevConfig"
app = Flask(__name__)

migrate = Migrate(app, db, compare_type=True)
app.config.from_object(f"blog.configs.{cfg_name}")
app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(articles_app, url_prefix="/articles")
app.register_blueprint(authors_app, url_prefix="/authors")
app.register_blueprint(auth_app, url_prefix="/auth")

# app.config["SECRET_KEY"] = "abcdefg123456"
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

admin.init_app(app)
db.init_app(app)
api = init_api(app)
login_manager.init_app(app)
flask_bcrypt.init_app(app)


@app.route("/")
def index():
    return render_template("index.html")
