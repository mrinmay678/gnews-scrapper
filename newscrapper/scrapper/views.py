from rest_framework.views import APIView
from rest_framework.response import Response
from .models import News

class NewsView(APIView):
    
    base_url="https://news.google.com/"
    url = f"{base_url}search?q=nri&hl=en-IN&gl=IN&ceid=IN%3Aen"

    def get(self, request):
        obj=News()
        res=obj.get()
        obj.close()
        return Response({"message":"Success","data":res,"status":True})
