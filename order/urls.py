from django.urls import path
from .import views


urlpatterns = [

    path('cart/', views.cart,name='cart'),
    path('addtocart/', views.addtocart,name='addtocart'),
    path('removeitem/<pk>',views.removeitem,name='removeitem'),
    path('checkout/',views.checkout,name='checkout'),
    path('orderform/',views.orderform,name='orderform'),
    path('orders/',views.orders,name='orders'),

]