from django.shortcuts import render

def index(request):
    return render(request, 'online_test/online_test.html')


