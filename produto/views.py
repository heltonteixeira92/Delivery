from django.http import HttpResponse
from django.shortcuts import render # noqa


def home(requests):
    return HttpResponse('Olá')
