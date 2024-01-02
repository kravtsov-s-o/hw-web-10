from django.shortcuts import render, redirect
import json
from quotes_list.models import Author, Tag, Quote
from datetime import datetime

def main(request):
    return render(request, 'scraping/index.html')


def uploadauthors(request):
    if request.method == 'POST' and request.FILES['json_file']:
        json_file = request.FILES['json_file']
        data = json.load(json_file)

        for item in data:
            author = Author.objects.create(
                fullname=item['fullname'],
                born_date=datetime.strptime(item['born_date'], "%B %d, %Y"),
                born_location=item['born_location'],
                description=item.get('description', '')
            )

        return redirect(to='quotes_list:authors')

    return render(request, 'scraping/index.html')

def auploadquotes(request):
    if request.method == 'POST' and request.FILES['json_file']:
        json_file = request.FILES['json_file']
        data = json.load(json_file)

        for item in data:
            # Получение id автора по fullname
            author_id = Author.objects.get(fullname=item['author']).id

            # Создание или получение тегов
            tags = [Tag.objects.get_or_create(name=tag)[0] for tag in item['tags']]

            # Создание цитаты
            quote = Quote.objects.create(
                author_id=author_id,
                quote=item['quote']
            )

            # Добавление тегов к цитате
            quote.tags.set(tags)

        return redirect(to='quotes_list:main')

    return render(request, 'scraping/index.html')
