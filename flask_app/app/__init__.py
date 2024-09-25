#!/usr/bin/env python
from config import Config
from flask import Flask
from sqlalchemy.orm import sessionmaker

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Import the database
    from app.database import Base, engine

    # NOTE: sqlsession vs session usage: session is a login/logout browser session while sqlsession is a Session() object
    # Create the database tables with the engine
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    sqlsession = Session()
    conn = engine.connect()

    # Initialize Flask extensions here

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.register import bp as register_bp
    app.register_blueprint(register_bp)

    # @app.route('/test/')
    # def test_page():
    #     return '<h1>Testing the Flask Application Factory Pattern</h1>'
        
    return app