from django.shortcuts import render

# Create your views here.

def homePageView(request):
    return render(request, 'testapp1/home.html')

def contactPageView(request):
    return render(request, 'testapp1/contact.html')