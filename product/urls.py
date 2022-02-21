from django.contrib import admin
from django.urls import path
from product import views



urlpatterns = [

    path('form',views.product_Form, name=''),
    path('bform',views.buy, name='') ,
    path('bform/<int:p_id>',views.display_Form, name=''),

]
