from django.shortcuts import render

def dorks(request):
    print("User Request : ", request)
    return render(request, 'advance_search.html', {})

def google(request):
    print("User Request : ", request)
    return render(request, 'google_search.html', {})

def shodan(request):
    print("User Request : ", request)
    return render(request, 'shodan_search.html', {})

def yandex(request):
    print("User Request : ", request)
    return render(request, 'yandex_search.html', {})

def bing(request):
    print("User Request : ", request)
    return render(request, 'bing_search.html', {})

def duck(request):
    print("User Request : ", request)
    return render(request, 'duck_search.html', {})