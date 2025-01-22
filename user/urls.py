from django.urls import path,include
from .import views
from django.conf.urls.static import static
from django.conf import Settings



urlpatterns = [

    path('',views.index,name='index'),
    path('account/',views.account,name='account'),
    path('cart/', views.cart,name='cart'),
    path('products/', views.products,name='products'),
    path('details-page/<int:pk>/', views.product_details,name='details-page'),
    path('logout/', views.sign_out,name='logout'),
    path('addtocart/', views.addtocart,name='addtocart'),
    path('removeitem/<pk>',views.removeitem,name='removeitem'),
    path('orderform/',views.orderform,name='orderform'),
    path('checkout/',views.checkout,name='checkout'),
    path('orders/',views.orders,name='orders'),
    path('profile-creation/', views.profile_creation, name='profile-creation'),

]


urlpatterns_api = [

]

urlpatterns += urlpatterns_api