from django.shortcuts import render, get_object_or_404

from .models import Quote, Author, Tag

# Create your views here.
def main(request):
    quotes = Quote.objects.all()
    tags = Tag.objects.all()[:10]
    return render(request, 'quotes_list/index.html', {"quotes": quotes, 'tags': tags})

def author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'quotes_list/author.html', {"author": author})
