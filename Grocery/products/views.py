from django.shortcuts import render, get_object_or_404
from .models import Category


def home(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'category_detail.html', context)