import datetime

import razorpay
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from .forms import CommentForm
from .forms import NewUserForm, CheckoutForm
from .models import Product, Detail, comment, ProductPayment


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',
                  {'products': products})


def info(request, pk):
    info = Detail.objects.filter(id=pk)
    products = Product.objects.filter(id=pk)

    return render(request, 'info.html',
                  {'info': info, 'products': products})


def checkout(request, pk):
    if request.method == "POST":
        name = request.POST.get('name')
        form = CheckoutForm

        # create razorpay client
        client = razorpay.Client(auth=('rzp_test_IWzavywWt6XvLO', 'zcZGUNh26Lx8H2Y3mDaHfHMO'))

        # create order
        response_payment = client.order.create(dict(amount=100000,
                                                    currency='INR',
                                                    ))
        order_id = response_payment['id']
        order_status = response_payment['status']

        if order_status == 'created':
            payment = ProductPayment(
                name=name,
                amount=100,
                order_id=order_id
            )
            payment.save()
            response_payment['name'] = [name]

            form = CheckoutForm(request.POST or None)
            products = Product.objects.filter(id=pk)
            return render(request, 'checkout.html', {'form': form,
                                                     'products': products, 'payment': response_payment})
    form = CheckoutForm
    products = Product.objects.filter(id=pk)
    return render(request, 'checkout.html',
                  {'form': form, 'products': products})

def payment_status(request):
    response = request.POST
    params_dict = {
        'razorpay_order_id': response['razorpay_order_id'],
        'razorpay_payment_id': response['razorpay_payment_id'],
        'razorpay_signature': response['razorpay_signature']
    }

    client = razorpay.Client(auth=('rzp_test_IWzavywWt6XvLO', 'zcZGUNh26Lx8H2Y3mDaHfHMO'))

    try:
        status = client.utility.verify_payment_signature(params_dict)
        ProductPayments = ProductPayment.objects.get(order_id=response['razorpay_order_id'])

        ProductPayments.razorpay_payment_id = response['razorpay_payment_id']
        ProductPayments.paid = True
        ProductPayments.save()

        return render(request, 'payment_status.html', {'status': True})

    except:
        return render(request, 'payment_status.html', {'status': True})


def register_request(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/products')
    else:
        form = NewUserForm()
    return render(request, 'register.html', {'form': form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/products")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("/products")


def home(request):
    return render(request, 'base.html')


def add_comment(request, pk):
    products = Product.objects.get(id=pk)
    form = CommentForm(instance=products)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=products)
        if form.is_valid():
            name = request.user.username
            body = form.cleaned_data['comment_body']

            c = comment(product=products, commenter_name=name, comment_body=body, date_added=datetime.datetime.now)
            c.save()
            return redirect('products')
        else:
            print('form is invalid')
    else:
        form = CommentForm()

    context = {
        'form': form
    }

    return render(request, 'add_comment.html', context)
