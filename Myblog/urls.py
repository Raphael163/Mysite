from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("about", views.about, name='about'),
    path("create", views.CreateView.as_view(), name='create'),
    # path("price", views.price, name='price.html'),
    # path("support", views.support, name='support.html')
]
