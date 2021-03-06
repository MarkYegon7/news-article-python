import os 

class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_KEY = '43728a6ff9584c9baa59768c05c80b37'
    SECRET_KEY = '<Flask WTF Secret Key>'
    NEWS_API_BASE_URL ='https://newsapi.org/v2/top-headlines/sources?apiKey={}'


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}