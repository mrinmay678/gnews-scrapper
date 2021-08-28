from datetime import datetime, timedelta
import requests

dt=datetime.now()+timedelta(hours=1)

while True:
    if dt==datetime.now():
        print(requests.get("http://15.206.75.100:8000/news/update"))
        dt=datetime.now()+timedelta(hours=1)


