from django.shortcuts import render

from catalog.models import Product, Category


def product_list(request):
    context = {'product_list': Product.objects.all()}
    return render(request, 'catalog/product_list.html', context)

#criado na aula 22
def category(request,slug):
    category = Category.objects.get(slug=slug)
    context = {
        'current_category': category,
        'product_list': Product.objects.filter(category=category),
    }
    return render(request,'catalog/category.html', context)