import json
from django.shortcuts import render


def index(request):
    with open('catalog\categories.json', encoding='utf-8') as f:
        categories = json.load(f)
    return render(request, 'catalog/index.html', {'categories': categories})

def category_detail(request, category_id):
    with open("catalog\categories.json", encoding='utf-8') as f:
        categories = json.load(f)
    category = next((c for c in categories if c['id'] == category_id), None)
    if category:
        with open('catalog\products.json', encoding='utf-8') as f:
            products = json.load(f)
        category_products = [p for p in products if p['category_id'] == category_id]
        return render(request, 'catalog\category_detail.html', {'category': category, 'products': category_products})
    else:
        return render(request, '404.html')

def product_detail(request, product_id):
    with open('catalog\products.json', encoding='utf-8') as f:
        products = json.load(f)
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return render(request, 'catalog/product_detail.html', {'product': product})
    else:
        return render(request, '404.html')