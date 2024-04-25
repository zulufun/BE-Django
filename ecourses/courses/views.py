from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators import http


# Create your views here.
def index(request):
    return render(request,'index.html',context={ 'name':'Duc Phuc'})
