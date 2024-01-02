from django.urls import path
from . import views

app_name = 'quotes_list'

urlpatterns = [
    path('', views.main, name='main'),
    path('author/<int:author_id>', views.author, name='author'),
    path('add/tag', views.addtag, name='addtag'),
    path('add/author', views.addauthor, name='addauthor'),
    path('add/quote', views.addquote, name='addquote'),
    # path('note/', views.note, name='note'),
    # path('tag/', views.tag, name='tag'),
    # path('detail/<int:note_id>', views.detail, name='detail'),
    # path('done/<int:note_id>', views.set_done, name='set_done'),
    # path('delete/<int:note_id>', views.delete_note, name='delete'),
]