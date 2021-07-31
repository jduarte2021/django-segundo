from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from time import gmtime, strftime, localtime


def index(request):
    context = {
        "time": strftime("%d-%m-%Y %H:%M %p", localtime())
    }
    return render(request,'index.html', context)

def segundo(request):
    return render(request,"segundo.html")




