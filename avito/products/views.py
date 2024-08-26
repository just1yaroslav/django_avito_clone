from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from products.models import ProductModel
from products.forms import SearchProductForm


def products(request):
    products = ProductModel.objects.filter(status=ProductModel.ProductStatus.PUBLISHED)
    categories = ProductModel.objects.values_list('category', flat=True).distinct()

    # Делаем пагинацию
    pagination = Paginator(products, 5)
    page_number = request.GET.get('post')
    page_obj = pagination.get_page(page_number)

    # Делаем поиск
    return render(request, 'products/products.html', context={
        'products': products,
        'categories': categories,
        'page_obj': page_obj,
    })


def product_detail(request, post):
    product = get_object_or_404(ProductModel, slug=post)
    print(product.title)
    return render(request, 'products/detail_products.html', {
        'product': product,
        'test': 'Test message',
    })
