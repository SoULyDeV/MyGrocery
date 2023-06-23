from django.shortcuts import render, get_object_or_404
from .models import Category


def home(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'category_detail.html', {'category': category})