from django.urls import path
from .views import ListArticlesView, ArticleView

urlpatterns = [
    path('', ListArticlesView.as_view(), name='list_articles'),
    path('<slug:slug>', ArticleView.as_view(), name='article')
]
