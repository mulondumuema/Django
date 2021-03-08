from django.shortcuts import render

# Create your views here.

def homePageView(request):
    msg1='Welcome To Uplatz'
    names=['Irene', 'Mulondu', 'Kavenge', 'Muema']
    dict={'msg':msg1, 'names':names}
    return render(request, 'testapp1/home.html', dict)
