from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from yandex import Yandex

def dorks(request):
    print("User Request : ", request)
    return render(request, 'advance_search.html', {})

def google(request):
    print("User Request : ", request)
    return render(request, 'google_search.html', {})

def shodan(request):
    print("User Request : ", request)
    return render(request, 'shodan_search.html', {})
@csrf_exempt
def yandex(request):
    if request.method == 'GET':
        print("GET Request ")

    elif request.method == 'POST':
        print(request.body.decode('utf-8'))
        print(request)
        print(request.method)
        print(request.body)
        execute = Yandex('Test')
        execute.query()
    return render(request, 'yandex_search.html', {})

def bing(request):
    print("User Request : ", request)
    return render(request, 'bing_search.html', {})

def duck(request):
    print("User Request : ", request)
    return render(request, 'duck_search.html', {})