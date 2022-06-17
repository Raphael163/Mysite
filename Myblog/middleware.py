# -*- coding: utf-8 -*-

from django.shortcuts import render, HttpResponse
import json
from django.urls import reverse, resolve
from django.conf import settings

NOT_AUTH_REQUIRED_URLS = ['index', 'about']



class MyBlog():
    def __init__(self, get_response):
        self._get_response = get_response

    def __call__(self, request):
        url_name = resolve(request.path).url_name
        response = self._get_response(request)

        # один из примеров практического применения
        if not request.user.is_authenticated:
            if not settings.ALLOW_ANOMIM_TO_CREATE and url_name not in NOT_AUTH_REQUIRED_URLS:
                return render(request, "Myblog/401.html", status=401)

        return response

    def process_exception(self, request, exception):
        # если возникла ошибка (баг), то можно например записать его  в базу или умедомление отправить и пр
        pass

