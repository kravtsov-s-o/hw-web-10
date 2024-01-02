from django.urls import path
from . import views

app_name = 'quotes_list'

urlpatterns = [
    path('', views.main, name='main'),
    path('author/<int:author_id>', views.author, name='author'),
    path('authors', views.authors, name='authors'),
    path('add/tag', views.addtag, name='addtag'),
    path('add/author', views.addauthor, name='addauthor'),
    path('add/quote', views.addquote, name='addquote'),
]
