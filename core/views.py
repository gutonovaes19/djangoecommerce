from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #lista de produtos - extraido do index.html

    return render(request,'index.html')

