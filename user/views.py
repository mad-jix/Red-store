from django.shortcuts import render, get_object_or_404, redirect,get_list_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from product.models import Products
from customer.models import Customer
from order.models import Order, CartItems
from order.forms import OrderForm


def index(request):
    products_list = {'products': Products.objects.all()}
    return render(request, 'index.html', products_list)


def account(request):
    context = {}
    if request.method == 'POST':
        if 'register' in request.POST:
            context['register'] = True
            try:
                username = request.POST.get('username')
                password = request.POST.get('password')
                email = request.POST.get('email')
                phone = request.POST.get('phone')
                address = request.POST.get('address')

                # Create user account
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    email=email
                )
                # Create customer account
                Customer.objects.create(
                    name=username,
                    user=user,
                    phone=phone,
                    address=address
                )
                messages.success(request, "Account created successfully. Please log in.")
                return redirect('account')
            except Exception as e:
                messages.error(request, "Error creating account. Please check your input.")
        elif 'login' in request.POST:
            context['register'] = False
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, "Invalid credentials. Please register first.")
    return render(request, 'account.html', context)


def sign_out(request):
    logout(request)
    return redirect('index')


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
        return redirect('profile-creation')  # Replace this with an actual profile creation view URL


def addtocart(request):
    if request.method == 'POST':
        user = request.user
        if hasattr(user, 'profile'):
            customer = user.profile
            quantity = int(request.POST.get('quantity'))
            product_id = request.POST.get('product_id')
            cart_obj, created = Order.objects.get_or_create(
                owner=customer,
                orderstatus=Order.CART_STAGE
            )
            product = get_object_or_404(Products, pk=product_id)
            order_item, created = CartItems.objects.get_or_create(
                product=product,
                owner=cart_obj,
            )
            order_item.quantity += quantity
            order_item.save()
            messages.success(request, "Item added to cart.")
        else:
            messages.error(request, "You need to create a profile to add items to the cart.")
    return redirect('cart')


def removeitem(request, pk):
    item = get_object_or_404(CartItems, pk=pk)
    item.delete()
    messages.success(request, "Item removed from cart.")
    return redirect('cart')


def products(request):
    products_list = {'products': Products.objects.all()}
    return render(request, 'products.html', products_list)


def product_details(request,pk):
    product = get_list_or_404(Products,pk=pk)
    print('iage',product)
    return render(request,'product_details.html',{'product':product}) 


def orderform(request):
    form = OrderForm()
    return render(request, 'orderform.html', {'form': form})


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
  

def profile_creation(request):
    if request.method == 'POST':
        pass
    return render(request, 'account.html')
