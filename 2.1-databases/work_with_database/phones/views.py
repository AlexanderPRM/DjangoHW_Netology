from django.shortcuts import render, redirect
from .models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    if sort == 'max_price':
        context = {'phones': Phone.objects.order_by('price')}
    elif sort == 'name':
        context = {'phones': Phone.objects.order_by('name')}
    elif sort == 'min_price':
        context = {'phones': Phone.objects.order_by('price')[::-1]}
    else:
        context = {'phones': Phone.objects.all()}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone': Phone.objects.get(slug=slug)}
    return render(request, template, context)
