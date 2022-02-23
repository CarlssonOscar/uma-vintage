from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category
from .forms import ProductForm


def all_products(request):
    """ Shows all products, will include sorting and search queries as well """

    products = Product.objects.filter(stock__gte=1)
    search_query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    if request.GET:
        if 'sq' in request.GET:
            search_query = request.GET['sq']
            if not search_query:
                messages.error(request, "Please enter a search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=search_query) | Q(description__icontains=search_query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': search_query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """ Shows details of a product """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)


def add_product(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, 'A new product was successfully added!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'The product could not be added. Please ensure the form input is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_product(request, product_id):
    """ Edit an existing product  """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.info(request, 'Updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Ensure the form input is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'Editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)