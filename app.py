from flask import Flask,render_template
import requests
 
api_key="b0f75ce660c0466a9a98c2478f8abb62" #enter your api key here
 
app = Flask(__name__)
 

 
@app.route('/')

def bbc():
    main_url =f"https://newsapi.org/v2/top-headlines?country=in&apiKey="+api_key # fetches top headlines from india 
    news = requests.get(main_url).json()  # renders result in a json format                                                          
    article = news['articles']  #get the articles from the topheadlines 
 
    desc = []
    news = []
    img = []
    link=[]
    myarticle=[]
 
   for i in range(len(article)): #iterate over the articles key fetched from news["articles"]
        myarticle = article[i]
 
 
        news.append(myarticle['title'])
        desc.append(myarticle['description'])
        img.append(myarticle['urlToImage'])
        link.append(myarticle['url'])
    my_list = zip(news, desc, img,link)  # zip method yield n length tuples  where n represents the positional arguments 

    return render_template('bbc.html', context =my_list)

if __name__=="__main__":
    app.run(debug=True)
