from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.core.paginator import Paginator
from django.db.models import Q

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    query = request.GET.get('query')

    # Fetch featured products
    featured_products = Product.objects.filter(is_featured=True, available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))
        
    paginator = Paginator(products, 6)  # Show 10 products per page
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    
    return render(request, 'productlist.html', {
        'category': category,
        'categories': categories,
        'products': products,
        'query': query,
        'featured_products': featured_products,  # Add this line
    })
    
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
    return render(request, 'productDetail.html', {
        'product': product,
        'related_products': related_products
    })