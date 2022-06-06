from django.shortcuts import render


def post_list(request):
    return render(request, "Myblog/post_list.html")


def about(request):
    return render(request, "Myblog/about.html")
