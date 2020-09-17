from app import app
import urllib.request,json
from .models import news
News = news.News

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url_news = app.config["NEWS_API_BASE_URL"]

# Getting the news base url
base_search_url_news = app.config['NEWS_API_SEARCH_URL']

def get_news(country):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url_news.format(country)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)


    return news_results

def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain movie details

    Returns :
        news_results: A list of movie objects
    '''
    news_results = []
    for news_item in news_list:
        title = news_item.get('title')
        description = news_item.get('description')
        date = news_item.get('publishedAt')
        url = news_item.get('url')
        img = news_item.get('urlToImage')
        content = news_item.get('content')

        if img:
            news_object = News(title,description,date,img, url, content)
            news_results.append(news_object)

    return news_results

def search_news(news_keyword):
    search_news_url = base_search_url_news.format(news_keyword)
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_results = None

        if search_news_response['articles']:
            search_news_list = search_news_response['articles']
            search_news_results = process_results(search_news_list)


    return search_news_results