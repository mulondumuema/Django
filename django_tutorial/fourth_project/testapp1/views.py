from django.shortcuts import render, HttpResponse

# Create your views here.
def homePageView(request):
    h1 = '<h1>Welcome To Uplatz</h1>'
    return HttpResponse(h1)


def aboutPageView(request):
    h1 = '<h1>About Us</h1>'
    return HttpResponse(h1)

def servicesPageView(request):
    h1 = '<h1>Services Offered</h1>'
    return HttpResponse(h1)

def contactPageView(request):
    h1 = '<h1>Contact Us</h1>'
    return HttpResponse(h1)
