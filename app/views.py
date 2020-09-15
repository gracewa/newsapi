from flask import render_template
from app import app
from newsapi import NewsApiClient


# Views
@app.route('/')
def index():
    newsapi=NewsApiClient(api_key='dbfa40f35ae24c188d04adfd4ebbd2a3')
    topheadlines = newsapi.get_top_headlines(sources='al-jazeera-english')
    articles = topheadlines['articles']
    titles = []
    descriptions = []
    imgs = []

    for i in range(len(articles)):
        newsarticles=articles[i]
        titles.append(newsarticles['title'])
        descriptions.append(newsarticles['description'])
        imgs.append(newsarticles['urlToImage'])

    newslist = zip(titles, descriptions, imgs)
    for title, description, img in newslist:
        print(title, description, img)

        return render_template('index.html', title=title, description=description, img=img)

