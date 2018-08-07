from django.shortcuts import render


# Create your views here.

def index(request):
    #lista de produtos - extraido do index.html
    texts = ['loren ipsum','consectetur adipisicing elit', 'sed do eiusmod tempor incididunt',
             'ut labore et dolore magna aliqua']
    #dicionadio - cchave e valor
    context = {
        'title':'django e-commerce',
        'texts' : texts
    }
    return render(request,'index.html', context)

