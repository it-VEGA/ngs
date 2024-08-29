from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def news(request):
    return render(request, 'home/news.html')

def tests(request):
    return render(request, 'home/test.html')
