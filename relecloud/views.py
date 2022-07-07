from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('욕쟁이 유진 & 지혜')
