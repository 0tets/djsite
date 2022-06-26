from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

def index(request):
    return HttpResponse("Страница приложения women.")

def categories(request, catid):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")

def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=False)

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def PageNotFound(request, exception):
    return HttpResponseNotFound("Страница не найдена")