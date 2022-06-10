from django.shortcuts import render
from .models import Task
from .models import Post


def index(request):
    tasks = Task.objects .all()
    return render(request, "Myblog/index.html", {"title": 'Главная страница сайта', 'tasks': tasks})


def about(request):
    posts = Post.objects .all()
    return render(request, "Myblog/about.html", {"title": 'Страница о нас', 'posts': posts})

# Подключение шаблонов без модели
# def index(request):
#     return render(request, "Myblog/index.html")
#
#
# def about(request):
#     return render(request, "Myblog/about.html")

# templates off
# def price(request):
#     return render(request, "Myblog/price.html")
#
#
# def support(request):
#     return render(request, "Myblog/support.html")
