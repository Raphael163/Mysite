from django.shortcuts import render
from .models import Task
from .models import Post
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()
    return render(request, "Myblog/index.html", {"title": 'Главная страница сайта', 'tasks': tasks})


def about(request):
    posts = Post.objects.all()
    return render(request, "Myblog/about.html", {"title": 'Страница о нас', 'posts': posts})


def create(request):
    error = ""
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()

        else:
            error = "Форма неверна"

    form = TaskForm
    context = {
        "form": form,
        "error": error
    }
    return render(request, "Myblog/create.html", context)

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
