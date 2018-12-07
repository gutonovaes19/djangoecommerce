from django.shortcuts import render
from django.http import HttpResponse

from catalog.models import Category

# Create your views here.

def index(request):
    # lista de produtos - extraido do index.html
    texts = ['Lorem ipsum', 'dolor sit amet', 'consectetur adipisicing elit',
             'sed do eiusmod ', 'tempor incididunt ut labore', 'et dolore magna aliqua']
    context = {
        'categories': Category.objects.add(),
    }

    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')


def product(request):
    return render(request, 'product.html')


def product_list(request):
    return render(request, 'product_list.html')


