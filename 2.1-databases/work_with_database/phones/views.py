from django.shortcuts import render, redirect, get_object_or_404

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    filter = request.GET.get('sort')

# настроим фильтры сортировки
    if filter == 'max_price':
        phones = Phone.objects.order_by('-price')
    elif filter == 'min_price':
        phones = Phone.objects.order_by('price')
    elif filter == 'name':
        phones = Phone.objects.order_by('name')
    else:
        phones = Phone.objects.all()

    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, sluggy):
    template = 'product.html'
    phone = get_object_or_404(Phone, slug=sluggy)
    context = {'phone': phone}
    return render(request, template, context)
