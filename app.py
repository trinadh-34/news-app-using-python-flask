from flask import Flask, render_template
from newsapi import NewsApiClient
 
 
app = Flask(__name__)
 

@app.route('/')
def bbc():
    newsapi = NewsApiClient(api_key="b0f75ce660c0466a9a98c2478f8abb62")
 #After registration on newsapi the apikey should be entered here
    topheadlines = newsapi.get_top_headlines(sources="bbc-news")#Gets top headlines from bbc news
 
    articles = topheadlines['articles']
 
    desc = []
    news = []
    img = []
 
    for i in range(len(articles)):
        myarticles = articles[i]
 
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
 
    mylist = zip(news, desc, img)
 
    return render_template('bbc.html', context=mylist)
 
if __name__=="__main__":
    app.run(debug=True)