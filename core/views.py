from django.shortcuts import render
from django.http import HttpResponse

from catalog.models import Category #10/12/2018 - aula 20

# Create your views here.

def index(request):
    #mostrar no menu as categorias -m 10-12-2018 aula 20
    context = {
        'categories': Category.objects.all()
    }

    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')


def product(request):
    return render(request, 'product.html')





