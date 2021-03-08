from django.shortcuts import render, HttpResponse

# Create your views here.
def f1(request):
    h2 = '<h2>Welcome To F1() View'
    return HttpResponse(h2)