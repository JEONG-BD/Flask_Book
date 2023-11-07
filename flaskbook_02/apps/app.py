from flask import Flask 
from flask_migrate import Migrate 
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path 
from flask_wtf.csrf import CSRFProtect 

db = SQLAlchemy()
csrf = CSRFProtect()
def create_app():
    app = Flask(__name__) 
    app.config.from_mapping(
        SECRET_KEY = '2AZSMss3p05QpbcY2hBsJ',
        SQLALCHEMY_DATABASE_URI = 
            f"sqlite:///{Path(__file__).parent.parent / 'local.sqllite'}", 
        SQLALCHEMY_TRACK_MODIFICATIONS = False,
        SQLALCHEMY_ECHO = True,
        WTF_CSRF_SECRET_KEY = 'AuwzyszUgugKN&KZs6f'
        
    )

    csrf.init_app(app)
    from apps.crud import views as crud_views

    app.register_blueprint(crud_views.crud, url_prefix="/crud")
    db.init_app(app)
    Migrate(app, db)
    return app 
     