from app import app
import urllib.request,json
from .models import news, sources

News = news.News
Sources = sources.Sources

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url_news = app.config["NEWS_API_BASE_URL"]

# Getting the news base url
base_url_search = app.config['NEWS_API_SEARCH_URL']

# Getting the sources base url
base_url_sources = app.config['NEWS_API_SOURCE_URL']

# Getting the top headlines base url
base_url_headlines = app.config['TOP_HEADLINES_URL']


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
    search_news_url = base_url_search.format(news_keyword)
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_results = None

        if search_news_response['articles']:
            search_news_list = search_news_response['articles']
            search_news_results = search_process_results(search_news_list)


    return search_news_results

def search_process_results(search_news_list):
    '''
    Function  that processes the search result and transform them to a list of Objects

    Args:
        search_news_list: A list of dictionaries that contain movie details

    Returns :
        search_news_results: A list of movie objects
    '''
    search_news_results = []
    for search_item in search_news_list:
        title = search_item.get('title')
        description = search_item.get('description')
        date = search_item.get('publishedAt')
        url = search_item.get('url')
        img = search_item.get('urlToImage')
        content = search_item.get('content')

        if img:
            search_news_object = News(title,description,date,img, url, content)
            search_news_results.append(search_news_object)

    return search_news_results

def get_sources():
    with urllib.request.urlopen(base_url_sources) as url2:
        sources_data = url2.read()
        sources_response = json.loads(sources_data)

        sources_results = None

        if sources_data:
            sources_list = sources_response['sources']
            sources_results = sources_process_results(sources_list)


    return sources_results

def sources_process_results(sources_list):
    '''
    Function  that processes the search result and transform them to a list of Objects

    Args:
        search_news_list: A list of dictionaries that contain movie details

    Returns :
        search_news_results: A list of movie objects
    '''
    sources_results = []
    for source in sources_list:
        id = source.get('id')
        name = source.get('name')
        description = source.get('description')
        url = source.get('url')
        sources_object = Sources(id,name,description,url)
        sources_results.append(sources_object)

    return sources_results


def top_headlines(selected_source):
    top_headlines_url = base_url_headlines.format(selected_source)
    with urllib.request.urlopen(top_headlines_url) as url:
        top_headlines_data = url.read()
        top_headlines_response = json.loads(top_headlines_data)

        top_headlines_results = None

        if top_headlines_response['articles']:
            top_headlines_list = top_headlines_response['articles']
            top_headlines_results = top_headlines_process_results(top_headlines_list)


    return top_headlines_results


def top_headlines_process_results(top_headlines_list):
    '''
    Function  that processes the search result and transform them to a list of Objects

    Args:
        search_news_list: A list of dictionaries that contain movie details

    Returns :
        search_news_results: A list of objects
    '''
    top_headlines_results = []
    for item in top_headlines_list:
        title = item.get('title')
        description = item.get('description')
        date = item.get('publishedAt')
        url = item.get('url')
        img = item.get('urlToImage')
        content = item.get('content')

        if img:
            top_headlines_object = News(title,description,date,img, url, content)
            top_headlines_results.append(top_headlines_object)

    return top_headlines_results
