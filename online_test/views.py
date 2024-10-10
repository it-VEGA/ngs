from django.shortcuts import render
import json

def index(request):
    return render(request, 'online_test/online_test.html')

def classes(request):
    return render(request, 'online_test/class.html')

def items(request, number):
    with open('online_test/static/online_test/items.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)["items"]
    if number == 5:
        exclude_subjects = ["Алгебра", "Геометрия","Химия"]
        filtered_data = [item for item in data if item['name'] not in exclude_subjects]
        return render(request, 'online_test/items.html', {'data': filtered_data})
    
def item_detail(request,pk,number):
    if pk == 'english':
        with open('online_test/static/online_test/russ.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            return render(request, 'online_test/item_detail.html', {'data': data})
    elif pk == 'informatika':
        with open('online_test/static/online_test/infor.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            return render(request, 'online_test/item_detail.html', {'data': data})
   


