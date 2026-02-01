from django.shortcuts import render, get_object_or_404
from .models import Phone

def phone_list(request):
    phones = Phone.objects.all()
    sort = request.GET.get('sort', 'name')
    if sort == 'min_price':
        phones = phones.order_by('price')
    elif sort == 'max_price':
        phones = phones.order_by('-price')
    else:
        phones = phones.order_by('name')
    return render(request, 'catalog.html', {'phones': phones})

def phone_detail(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    return render(request, 'product.html', {'phone': phone})