from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
<<<<<<< HEAD

db = SQLAlchemy()
migrate = Migrate()

"""THe responsibility of create_app is to:
-Connect Flask to our sapphire_flasky_development db
    - setting up SQLAlchemy and Migrate to do its thing
-Regist our blueprints (our routes)
"""
=======
>>>>>>> 4efb54e2954eef756f1632bee5988982a6294328

db = SQLAlchemy()
migrate = Migrate()

"""
The responsibility of create_app is to:
- Connect Flask to our sapphire_flasky_development db
    - setting up SQLAlchemy and Migrate to do its thing
- Register our blueprints (our routes)
"""
def create_app():

    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:postgres@localhost:5432/sapphire_flasky_development"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
<<<<<<< HEAD
    migrate.init_app(app,db)

    from app.models.animal import Animal

=======
    migrate.init_app(app, db)


    from app.models.animal import Animal


>>>>>>> 4efb54e2954eef756f1632bee5988982a6294328
    #  add our new animals blueprint
    from flask import Blueprint
    from .routes.animal import animals_bp

    app.register_blueprint(animals_bp)

    return app 
