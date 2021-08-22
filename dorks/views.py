from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from selenium import webdriver
from pathlib import Path

def convert(lst):
    res_dct = {"data" : lst[i] for i in range(0, len(lst))}
    print(res_dct)
    return res_dct

def getFile():
    path = Path(__file__).parent / "dorks.txt"
    file = open(path , "r")
    return file.readlines()

def dorks(request):
    print("User Request : ", request)
    return render(request, 'advance_search.html', {})

@csrf_exempt
def google(request):
    if request.method == 'GET':
        print("GET Request ")
        data = getFile()
        context = {
            "object_list": data
        }
        return render(request, "google_search.html",context)
    elif request.method == 'POST':
        print("decode ", request.POST['inputcommand'])
        try:
            driver = webdriver.Firefox()
            driver.get("http://www.google.com")
            print(request.POST['inputcommand'])
            driver.find_element_by_id("L2AGLb").click();
            input_element = driver.find_element_by_name("q")
            input_element.send_keys(str(request.POST['inputcommand']))
            input_element.submit()
            print("google query execution ", request.POST['inputcommand'])
            data = getFile()
            context = {
                "object_list": data
            }
        except ValueError:
            pass
        return render(request, 'google_search.html', context)

@csrf_exempt
def shodan(request):
    if request.method == 'GET':
        print("GET Request ")
        return render(request, "shodan_search.html")
    elif request.method == 'POST':
        print("decode ", request.POST['inputcommand'])
        try:
            driver = webdriver.Firefox()
            query = "https://www.shodan.io/search?query=" + str(request.POST['inputcommand'])
            print("shodan query execution ", request)
            driver.get(query)
        except ValueError:
            pass
        return render(request, 'shodan_search.html')
@csrf_exempt
def yandex(request):
    if request.method == 'GET':
        print("GET Request ")
        return render(request, "yandex_search.html")
    elif request.method == 'POST':
        print("decode ", request.POST['inputcommand'])
        try:
            driver = webdriver.Firefox()
            query = "https://yandex.com/search/?text=" + str(request.POST['inputcommand'])
            print("Yandex query execution ", request)
            driver.get(query)
        except ValueError:
            pass
        return render(request, 'yandex_search.html')

@csrf_exempt
def bing(request):
    if request.method == 'GET':
        print("GET Request ")
        return render(request, "bing_search.html")
    elif request.method == 'POST':
        print("decode ", request.POST['inputcommand'])
        try:
            driver = webdriver.Firefox()
            driver.get("http://www.bing.com")
            input_element = driver.find_element_by_name("q")
            input_element.send_keys(str(request.POST['inputcommand']))
            input_element.submit()
        except ValueError:
            pass
        return render(request, 'bing_search.html', {})

@csrf_exempt
def duck(request):
    if request.method == 'GET':
        print("GET Request ")
        return render(request, "duck_search.html")
    elif request.method == 'POST':
        print("decode ", request.POST['inputcommand'])
        try:
            driver = webdriver.Firefox()
            driver.get("https://duckduckgo.com/")
            input_element = driver.find_element_by_name("q")
            input_element.send_keys(str(request.POST['inputcommand']))
            input_element.submit()
        except ValueError:
            pass
        return render(request, 'duck_search.html', {})