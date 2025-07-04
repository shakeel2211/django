from django.http import HttpResponse
from django.shortcuts import render



def home(request):
  # return HttpResponse("Welcome to the home page!")
  return render(request , "index.html")


def about(request):
   return HttpResponse("Welcome to the about page!")


def contact(request):
   return HttpResponse("Welcome to the contact page!")
