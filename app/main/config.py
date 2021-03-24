"""
Configuration script of system environment variables according to the different profiles of the application
"""
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'w%;!V6N{JG#^l>`W%woL`Zp{@UO*g')
    DEBUG = False
    LOG_TYPE = 'file'
    APP_LOG_NAME = 'hotel-backend-rest.log'
    WWW_LOG_NAME = 'hotel-navigation.log'
    LOG_MAX_BYTES = 100_000_000
    LOG_COPIES = 5
    ENABLED_MODULES = ['auth', 'user', 'shared', 'hotel', 'administration', 'room']
    JWT_SECRET_KEY = 'z8DUpH4ex5'
    JWT_ACCESS_TOKEN_EXPIRES = 28800
    JWT_ALGORITHM = 'HS512'
    JWT_USER_CLAIMS = 'hotel-jwt-object'
    JWT_HEADER_NAME = 'Authorization'
    RECOVER_PASSWORD_TOKEN_EXPIRES = 7200
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    LOG_LEVEL = 'INFO'
    LOG_DIR = 'C:/var/log/hotel'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/hotel'
    SQLALCHEMY_ECHO = True


class TestConfig(Config):
    DEBUG = True
    TESTING = True
    LOG_LEVEL = 'INFO'
    LOG_DIR = 'C:/var/log/hotel'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://gestprod:Cadena2020#@174.138.0.99/gestprod'


class StagingConfig(Config):
    DEBUG = True
    TESTING = True
    LOG_LEVEL = 'INFO'
    LOG_DIR = 'C:/var/log/hotel'
    SQLALCHEMY_DATABASE_URI = ''


class ProductionConfig(Config):
    DEBUG = False
    LOG_LEVEL = 'WARNING'
    LOG_DIR = 'C:/var/log/hotel'
    SQLALCHEMY_DATABASE_URI = ''


config_by_name = dict(
    development=DevelopmentConfig,
    testing=TestConfig,
    staging=StagingConfig,
    production=ProductionConfig
)
