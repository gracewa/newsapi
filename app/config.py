class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL ='https://newsapi.org/v2/top-headlines?country={}&apiKey=dbfa40f35ae24c188d04adfd4ebbd2a3'
    NEWS_API_KEY = 'dbfa40f35ae24c188d04adfd4ebbd2a3'
    NEWS_API_SEARCH_URL = 'https://newsapi.org/v2/everything?q={}&apiKey=dbfa40f35ae24c188d04adfd4ebbd2a3'
    NEWS_API_SOURCE_URL = 'https://newsapi.org/v2/sources?apiKey=dbfa40f35ae24c188d04adfd4ebbd2a3'




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
