from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def team(request):
    return render(request, 'home/team.html')
