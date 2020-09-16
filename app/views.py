from flask import render_template
from app import app
from newsapi import NewsApiClient
from .request import get_news


# Views
@app.route('/')
def index():
    '''
        View root page function that returns the index page and its data
    '''
    news_highlights = get_news('ng')
    title = 'Get the Latest News Fast'

    return render_template('index.html', title=title, news_highlights=news_highlights)

