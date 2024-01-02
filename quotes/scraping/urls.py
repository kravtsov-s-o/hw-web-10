from django.urls import path
from . import views

app_name = 'scraping'

urlpatterns = [
    path('scraping', views.main, name='scraping'),
    path('uploadauthors', views.uploadauthors, name='uploadauthors'),
    path('uploadquotes', views.auploadquotes, name='uploadquotes'),
]
