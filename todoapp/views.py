from django.shortcuts import render
from django.http import HttpResponse

def get_todo_page(request):
    return HttpResponse("Hello World")