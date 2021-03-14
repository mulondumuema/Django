from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
import json
def displayEmployeeDetails(request):
    emp = {
        'eid':1,
        'ename':'Irene',
        'ecity':'Nairobi',
    }
    json_data=json.dumps(emp)
    return HttpResponse(json_data, content_type='application/json')

from django.views.generic import View
from django.http import JsonResponse

class JsonView(View):
    def get(self,request,*args,**kwargs):
        emp = {
        'eid':1,
        'ename':'Irene',
        'ecity':'Nairobi'
        }
        return JsonResponse(emp)