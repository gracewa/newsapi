from flask import render_template,request,redirect,url_for
from app import app
from newsapi import NewsApiClient
from .request import get_news, search_news, get_sources, top_headlines



# Views
@app.route('/', methods=['GET', 'POST'])
def index():
    '''
        View root page function that returns the index page and its data
    '''
    news_highlights = get_news('us')
    title = 'Get the Latest News Fast'
    search_new = request.args.get('news_query')
    selected_source = 'selected_source'
    news_sources = get_sources()


    if search_new:
        return redirect(url_for('search', news_keyword=search_new))

    else:
        return render_template('index.html', title=title, news_highlights=news_highlights, news_sources=news_sources)


@app.route('/search/<news_keyword>', methods=['GET', 'POST'])
def search(news_keyword):
    '''
    View function to display the search results
    '''
    news_keyword_list = news_keyword.split(" ")
    news_keyword_format = "+".join(news_keyword_list)
    searched_news = search_news(news_keyword_format)
    title = f'Search Results for "{news_keyword}"'
    return render_template('search.html', title=title, searched_news=searched_news)


@app.route('/sources/<source_id>', methods=['GET', 'POST'])
def source_top_headlines(source_id):
    headlines = top_headlines(source_id)

    return render_template('headlines.html',  headlines=headlines, source_id=source_id)