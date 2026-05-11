from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

def home_view(request):
    return HttpResponse('<h1>hello my friend you in the home page</h1>')


def about_view(request):
    return HttpResponse('<h1>hello my friend you in the about page </h1>')


def contact_view(request):
    return HttpResponse('<h1>hello my friend you in the contact page</h1>')

# Create your views here.
