from django.shortcuts import render
from datetime import datetime

# Create your views here.

def homePageView(request):
    dict = {'msg':'welcome to uplatsz', 'date': datetime.now(), 'eid':1, 'ename': 'Irene', 'email':'mulondumuema@gmail.com'}
    return render(request, 'testapp1/home.html', dict )
