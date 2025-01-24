from django.urls import path
from .import views


urlpatterns = [

    path('products/', views.products,name='products'),
    path('details-page/<int:pk>/', views.product_details,name='details-page'),

]