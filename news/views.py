from django.shortcuts import render

from news.models import News


def index(request):
    news = News.objects.all()
    return render(request, 'news.html', {'news': news})


def news_detail(request, id):
    new = News.objects.get(pk=id)
    return render(request, 'news-detail.html', {'new': new})
