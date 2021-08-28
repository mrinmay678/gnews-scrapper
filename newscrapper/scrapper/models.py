import pymongo
from utils.db import Base
from bson.json_util import loads, dumps

class News(Base):

    def __init__(self):
        super().__init__()

    def save(self,obj):
        if not self.client.news.news.find_one({"link":obj['link']}):
            id=self.client.news.news.insert_one({
                "title":obj['details'],
                "link":obj['link'],
                "image":obj['image'],
                "time":obj['time']
            })
            self.client.news.news.update_one({"link":obj['link']},{"id":id})
    def get(self):
        return loads(dumps(self.client.news.news.find({},{"_id":False}).sort("time",pymongo.DESCENDING)))