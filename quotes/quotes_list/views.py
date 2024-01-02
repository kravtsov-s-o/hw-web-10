from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Quote, Author, Tag
from .forms import AddTag, AddAuthor, AddQuote


# Create your views here.
def main(request):
    tags_with_usage = Tag.objects.annotate(num_quotes=Count('tags'))
    sorted_tags = tags_with_usage.order_by('-num_quotes')
    tags = sorted_tags[:10]

    tag_name = request.GET.get('tag')

    if tag_name:
        quotes = Quote.objects.filter(tags__name=tag_name).order_by('-created')
    else:
        quotes = Quote.objects.all().order_by('-created')


    items_per_page = 10
    paginator = Paginator(quotes, items_per_page)

    page = request.GET.get('page')

    try:
        quotes_page = paginator.page(page)
    except PageNotAnInteger:
        quotes_page = paginator.page(1)
    except EmptyPage:
        quotes_page = paginator.page(paginator.num_pages)

    page_range = range(1, quotes_page.paginator.num_pages + 1)

    return render(request, 'quotes_list/index.html',
                  context={"quotes": quotes_page, 'page_range': page_range, 'tags': tags})


def author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'quotes_list/author.html', {"author": author})


@login_required
def addtag(request):
    tags = Tag.objects.all().order_by('-created')[:30]

    if request.method == 'POST':
        form = AddTag(request.POST)

        if form.is_valid():
            form.save()
            return redirect(to='quotes_list:addtag')
        else:
            return render(request, 'quotes_list/add/tag.html', {"form": form, 'tags': tags})

    return render(request, 'quotes_list/add/tag.html', context={'form': AddTag, 'tags': tags})


@login_required
def addauthor(request):
    if request.method == 'POST':
        form = AddAuthor(request.POST)

        if form.is_valid():
            instance = form.save()
            return redirect('quotes_list:author', author_id=instance.pk)
        else:
            return render(request, 'quotes_list/add/author.html', {"form": form})

    return render(request, 'quotes_list/add/author.html', context={'form': AddAuthor})


@login_required
def addquote(request):
    tags = Tag.objects.all()

    if request.method == 'POST':
        form = AddQuote(request.POST)

        if form.is_valid():
            new_quote = form.save()

            choise_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))

            for tag in choise_tags.iterator():
                new_quote.tags.add(tag)

            return redirect(to='quotes_list:main')
        else:
            return render(request, 'quotes_list/add/quote.html', {"form": form, 'tags': tags})

    return render(request, 'quotes_list/add/quote.html', context={'form': AddQuote, 'tags': tags})


def custom_404(request, exception):
    return render(request, '404.html', status=404)
