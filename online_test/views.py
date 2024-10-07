from django.shortcuts import render
import json

def index(request):
    return render(request, 'online_test/online_test.html')
def item(request):
    with open('online_test/static/online_test/russ.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        print(data)
    return render(request, 'online_test/item.html', {'data': data})


