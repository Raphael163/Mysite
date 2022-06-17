from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView

from .models import Task
from .models import Post
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()
    return render(request, "Myblog/index.html", {"title": 'Главная страница сайта', 'tasks': tasks})


def about(request):
    posts = Post.objects.all()
    return render(request, "Myblog/about.html", {"title": 'Страница о нас', 'posts': posts})


# вместо  create
class CreateView(TemplateView):
    template_name = 'Myblog/create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TaskForm()
        return context

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        context = self.get_context_data(**kwargs)
        if form.is_valid():
            form.save()

        else:
            context['error'] = "Форма неверна"
        context['form'] = TaskForm()
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        return self.render_to_response(context)


# неиспользуемое
def create(request):
    context, error = {}, ""
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            context['error'] = "Форма неверна"
        context['form'] = TaskForm()

    else:
        context['form'] = TaskForm()

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
