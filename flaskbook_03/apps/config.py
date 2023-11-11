import secrets 
from pathlib import Path


basedir = Path(__file__).parent.parent


class BaseConfig : 
    SECRET_KEY = '2AZSMss3p5QPbcY2hBsJ'
    WTF_CSRF_SECRET_KEY = 'AuwzyszU5sugKN7KZs6f'
    

class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'local.sqllite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    

class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'testing.sqllite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False 
    WTF_CSRF_ENABLED = False 

config = {
    "testing":TestingConfig ,
    "local" : LocalConfig
}
