from django.shortcuts import render, HttpResponseRedirect
from .models import Product, ProductCategory, Basket
from main.models import Users

def katalog(request):
    categories = ProductCategory.objects.all()
    return render(request, 'products/katalog.html', context={
        'categories': categories,
        }
                )

def products(request, pk):
    categories = ProductCategory.objects.all()
    category = ProductCategory.objects.get(pk=pk)
    products = category.products.all()
    return render(request, 'products/tovars.html', context={
        'products': products,
        'categories': categories,
        'category': category
        }
    )

def basket(request):
    baskets = Basket.objects.filter(user=request.user)
    total_quantity = 0
    for basket in baskets:
        total_quantity = total_quantity + basket.quantity
    context = {
        'baskets': Basket.objects.filter(user=request.user),
        'total_quantity': total_quantity,
    }
    return render(request, 'products/basket.html', context)



def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])