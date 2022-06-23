from django.shortcuts import render
from django.http import HttpResponse

def my_view(request):
    return HttpResponse("Belajar CRUD Django")
# Create your views here.
