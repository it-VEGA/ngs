from django.shortcuts import render

def news(request):
    return render(request, 'news/news.html')

def detail(request):
    return render(request, 'news/news-details.html')

