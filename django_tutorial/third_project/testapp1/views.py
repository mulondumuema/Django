from django.shortcuts import render, HttpResponse

# Create your views here.
def homePageView(request):
    return HttpResponse('<h2>Welcome To Uplatz</h2>')

def aboutPageView(request):
    return HttpResponse('<h2 style="color:red">About Page</h2>')