from django.shortcuts import render

from django.shortcuts import redirect

from product.forms import productForm

from product.models import Product



# Create your views here.

def buy(request):

    if request.method=="POST":

        forms=buyForm(request.POST)

        forms.save()

        return redirect ("/products")


    

    return render(request,'buy_form.html')

def product_Form(request):

    print("hh")



    if request.method=="POST":

        forms=productForm(request.POST,request.FILES)

        forms.save()

        return redirect ("/home")

    return render(request,'products_form.html')

def display_Form(request,p_id):
    products=Product.objects.get(product_id=p_id)
    return render(request,'buy_form.html',{'products':products})


