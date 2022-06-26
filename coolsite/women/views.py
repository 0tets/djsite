from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}]

def index(request):
    posts = Women.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, "women/index.html", context=context)

def about(request):
    context = {
        'menu': menu,
        'title': 'О сайте'
       }
    return render(request, "women/about.html", context=context)

def addpage(request):
    return HttpResponse("Добавление статьи")

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")
def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")
def PageNotFound(request, exception):
    return HttpResponseNotFound("Страница не найдена")