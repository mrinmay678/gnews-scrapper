from bs4 import BeautifulSoup
import requests
from .models import News
from celery import shared_task

@shared_task(bind=True)
def newsUpdate(self):
    base_url="https://news.google.com/"
    url = f"{base_url}search?q=nri&hl=en-IN&gl=IN&ceid=IN%3Aen"
    soup=BeautifulSoup(requests.get(url).text,"html.parser")
    obj=News()
    for i in soup.find_all('div',attrs={'class':"NiLAwe y6IFtc R7GTQ keNKEd j7vNaf nID9nc"}):
        news={}
        det=i.find('a', attrs={'class':'DY5T1d RZIKme'})
        news['details']=det.text
        news['link']=base_url+det['href'][2:]
        news['time']=i.find('time')["datetime"]
        news['image']=i.find('img',attrs={'class':'tvs3Id QwxBBf'})["src"]
        obj.save(news)
    obj.close()
    print("Success")