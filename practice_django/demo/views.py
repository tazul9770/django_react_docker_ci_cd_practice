from django.shortcuts import render
from django.http import HttpResponse

def test(request):
    return HttpResponse("Docker and ci cd pipeline done")
