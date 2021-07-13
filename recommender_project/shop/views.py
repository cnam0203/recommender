from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Transaction
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from json import dumps

# Create your views here.

def greeting(request):
    return HttpResponse('Hello')

def product_list(request):
    list_product = list(Product.objects.all())
    return HttpResponse(list_product)

def product(request, id):
    products = Product.objects.filter(id=id)
    product = list(products)[0]
    return HttpResponse('Product ' + product.name)

def add_product(request, name):
    new_product = Product.objects.create(name=name)
    new_product.save()
    return HttpResponse('New product id ' + str(new_product.id))

def introduction(request):
    return render(request, "shop/introduction.html")

def product_page(request, id):
    return render(request, "shop/product-page.html", { 'product': id, 'recommend_products': ['fish', 'vegetables', 'sausagges'] })

def report(request):
    total_transaction_by_date = list(Transaction.objects.values('date').annotate(total=Count('id')).order_by('date'))
    report_data = []

    if (len(total_transaction_by_date) != 0):
        report_data = [[row['date'].strftime("%d-%m-%Y"), row['total']] for row in total_transaction_by_date]

    chart = {
        'title': 'Total transaction by day',
        'data' : report_data
    }

    return render(request, "shop/report.html", { 'chart' : dumps(chart) })

def login_page(request):
    return render(request, "shop/login.html")

def login_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/shop/introduction')
    else:
        return render(request, "shop/login.html")

def logout_user(request):
    logout(request)
    return render(request, 'shop/login.html')

@login_required(login_url="/shop/login")
def get_data(request):
    return HttpResponse('Get data successfully')
