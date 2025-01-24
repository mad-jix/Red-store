from django.shortcuts import render, get_object_or_404, redirect,get_list_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



from product.models import Products
from customer.models import Customer


def index(request):
    products_list = {'products': Products.objects.all()}
    return render(request, 'index.html', products_list)


def account(request):
    context={}
    if request.POST and 'register' in request.POST:
        context['register']=True
        try:
            username=request.POST.get('username')
            password=request.POST.get('password')
            email=request.POST.get('email')
            phone=request.POST.get('phone number')
            address=request.POST.get('adress')
            #create user account
            user=User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            #creates customer account
            customer=Customer.objects.create(
                name=username,
                user=user,
                phone=phone,
                address=address
            )   
            return redirect('account') 
        except Exception as e:
            error_message="please check your data"
            messages.error(request,error_message)
    if request.POST and 'login' in request.POST:
        context['register']=False
        print(request.POST)
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request,'user not existing please register')
    return render(request,'account.html',context)

def sign_out(request):
    logout(request)
    return redirect('index')

def profile_creation(request):
    if request.method == 'POST':
        pass
    return render(request, 'account.html')
