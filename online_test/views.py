from django.shortcuts import render
import json

def index(request):
    return render(request, 'online_test/online_test.html')

def classes(request):
    return render(request, 'online_test/class.html')

def items(request):
   return render(request, 'online_test/items.html')
    
def item_detail(request,pk):
    if pk == 'english':
        with open('online_test/static/online_test/russ.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            return render(request, 'online_test/item_detail.html', {'data': data})
    elif pk == 'inforamtika':
        with open('online_test/static/online_test/infor.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            return render(request, 'online_test/item_detail.html', {'data': data})
   


