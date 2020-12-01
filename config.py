import os

class Config:

    COUNTRY_API_BASE_URL ='https://restcountries.eu/rest/v2/all'
    SECRET_KEY = '12345'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wecode:12345@localhost/worldboard'

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}