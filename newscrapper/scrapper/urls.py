from django.urls import path
from .views import NewsView

urlpatterns = [
    path('news/scrap', NewsView.as_view()),
]
