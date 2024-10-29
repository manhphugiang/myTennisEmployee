from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def members(request):
    template= loader.get_template('myfirst.html')
    return HttpResponse(template.render())


def members2(request):
    return HttpResponse("Hello This is Manh")


def manh(request):
    return HttpResponse("Hello This is Manh Phu Giang")