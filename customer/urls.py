from django.contrib import admin

from django.urls import path

from customer import views



urlpatterns = [
    path('register',views.register, name='register'),
    path('',views.signin, name='signin'),

    path('home',views.home, name='home'),
    path('admindashboard',views.admindashboard, name='admindashboard'),

    path('products',views.products, name='products'), 
    path('contact',views.contact, name='products'),
    path('about',views.about, name='about'),   
    path('blogs',views.blogs, name='blogs'),
    path('blogsform',views.blogsform, name='blogsform') ,
    path('productsform',views.productsform, name='productsform'),
    path('orders',views.orders, name='orders'),   
    path('ordered',views.ordered, name='ordered'),  

    
    path('purchaseitem/<int:product_id>/', views.purchaseitem, name="purchaseitem"),


]


