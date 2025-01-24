from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db import transaction

from product.models import Products

from .models import Order,CartItems
from .forms import OrderForm

def removeitem(request, pk):
    item = get_object_or_404(CartItems, pk=pk)
    item.delete()
    messages.success(request, "Item removed from cart.")
    return redirect('cart')

def addtocart(request):
    if request.method == 'POST':
        try:
            user = request.user
            if not hasattr(user, 'profile'):
                messages.error(request, "You need to create a profile to add items to the cart.")
                return redirect('cart')
            
            customer = user.profile
            product_id = request.POST.get('product_id')
            quantity = int(request.POST.get('quantity', 1)) 

            
            product = get_object_or_404(Products, pk=product_id)

            with transaction.atomic():
                cart_obj, created = Order.objects.get_or_create(
                    owner=customer,
                    orderstatus=Order.CART_STAGE,
                    defaults={
                        'name': customer.name or "Default Name",
                        'place': "Default Place",
                        'address': "Default Address",
                        'email': customer.user.email,
                        'phonenumber': 1234567890, 
                        'city': "Default City",
                    }
                )

                order_item, created = CartItems.objects.get_or_create(
                    product=product,
                    owner=cart_obj,
                )
                if not created:
                    order_item.quantity += quantity
                    order_item.save()

            messages.success(request, "Item added to cart.")
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('cart')
    return redirect('cart')

def cart(request):
    user = request.user
    if hasattr(user, 'profile'):
        customer = user.profile
        cart_obj, created = Order.objects.get_or_create(
            owner=customer,
            orderstatus=Order.CART_STAGE
        )
        context = {'cart': cart_obj}
        return render(request, 'cart.html', context)
    else:
        messages.error(request, "You need to create a profile to access the cart.")
        return redirect('profile-creation')
    
def removeitem(request, pk):
    item = get_object_or_404(CartItems, pk=pk)
    item.delete()
    messages.success(request, "Item removed from cart.")
    return redirect('cart')
    
def checkout(request):
    if request.method == 'POST':
        try:
            user = request.user
            if hasattr(user, 'profile'):
                customer = user.profile
                order_obj = Order.objects.get(
                    owner=customer,
                    orderstatus=Order.CART_STAGE
                )
                form = OrderForm(request.POST, instance=order_obj)
                if form.is_valid():
                    order_obj.orderstatus = Order.ORDER_PROCESSED
                    order_obj.save()
                    messages.success(request, "Your order is confirmed.")
                else:
                    messages.error(request, "Invalid order details.")
            else:
                messages.error(request, "You need to create a profile to place an order.")
        except Order.DoesNotExist:
            messages.error(request, "No active cart found.")
    return redirect('orders')

def orderform(request):
    form = OrderForm()
    return render(request, 'orderform.html', {'form': form})

def orders(request):
    user = request.user
    if hasattr(user, 'profile'):
        customer = user.profile
        all_orders = Order.objects.filter(owner=customer).exclude(orderstatus=Order.CART_STAGE)

        orders_with_items = []
        for order in all_orders:
            items = CartItems.objects.filter(owner=order)
            orders_with_items.append({
                'order': order,
                'items': items
            })
        
        context = {'orders_with_items': orders_with_items}
        return render(request, 'orders.html', context)
    else:
        messages.error(request, "You need to create a profile to view orders.")
        return redirect('profile-creation')