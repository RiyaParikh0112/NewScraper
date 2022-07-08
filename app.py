from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app=Flask(__name__)
@app.route('/',methods=["GET", "POST"])
def index():
    url = "https://www.businesstoday.in/crypto"
    req=requests.get(url)
    soup=BeautifulSoup(req.content,'html.parser')
    news_data=soup.find_all('div',class_='widget-listing',limit=5)
    LiveNews=""
    for data in news_data:
        news=data.div.div.a['title']
        LiveNews += "\u2022"+ news + "\n"
    return render_template('index.html',News=LiveNews)

