from dataclasses import dataclass
import imp
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from product.models import Product, Orders

from django.contrib.auth import get_user_model

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            user = User.objects.create_user(email=email, username=username, password=password)
            auth.login(request, user)
            user.save()
            return redirect('register')
        else:
            return redirect('register')

    return render(request, 'register.html')
   
def admindashboard(request):
    user = get_user_model()
    usercount = user.objects.all().filter(is_superuser=False).count()
    productcount = Product.objects.all().count()
    ordercount = Orders.objects.all().count()
    data = {
        'productcount':productcount,
        'ordercount':ordercount,
        'usercount':usercount,
    }
    return render(request,'admindashboard.html', data)


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user.is_superuser:
            auth.login(request, user)
            return redirect('admindashboard')
        elif user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return redirect('login')

    return render(request,'login.html')


def home(request):
    return render(request,'home.html')

def blogs(request):
    return render(request,'blogs.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def products(request):
     products=Product.objects.all()
     return render(request,'products.html',{'products':products})

def blogsform(request):
    return render(request,'blogs_form.html')

def productsform(request):
        return render(request,'products_form.html')


def orders(request):
    order=Booking.objects.all()
    return render(request,'catering_orders.html',{'order':order})

def ordered(request):
    return render(request,'ordered.html')

def purchaseitem(request, product_id):
    if request.method == "POST":
        current_user = request.user
        product = Product.objects.get(id=product_id)
        
        order = Orders(user=current_user, product=product)
        order.save()
        return redirect('ordered')