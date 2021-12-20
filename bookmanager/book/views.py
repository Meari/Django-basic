from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
"""
视图
    所谓的视图， 其实就是python的函数
视图有两个要求
    1. 视图函数的第一个参数就是接收请求。 这个请求其实就是HttpRequest的类对象
    2. 必须返回一个响应
"""


def index(request):
    return HttpResponse('ok')
