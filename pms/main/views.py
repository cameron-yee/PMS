from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django import forms
from django.contrib.auth.decorators import login_required
from .forms import * 
from django.contrib.auth.models import User
from .models import Contract


@login_required
def home(request):
    return render(request, 'main/home.html')

@login_required
def email(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            send_mail(
                'SUBJECT',
                'Hi Bob, here is a message.',
                'yee.camero23@gmail.com',
                ['yee.camero23@gmail.com'],
                fail_silently=False,
            )

            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, 'main/email.html', {'form': form})


@login_required
def order(request):
    if request.method == "POST":
        purchase_form = PurchaseOrderForm(request.POST)
        quote_form = QuoteForm(request.POST)
        price = 0
        quantity = 0.0
        saved_quote = 0
        saved_purchase = 0

        if quote_form.is_valid():
            finished_quote_form = quote_form.save(commit=False)
            price = quote_form.cleaned_data['QPrice']

            if purchase_form.is_valid():
                finished_purchase_form = purchase_form.save(commit=False)

                user_email = request.user.email
                send_mail(
                    'PURCHASE ORDER CONFIRMATION',
                    'Hi {}, you\'re purchase order form has been received.\n\nPurchase Management System'.format(request.user.first_name),
                    'yee.camero23@gmail.com',
                    [user_email],
                    fail_silently=False,
                )

                quantity = purchase_form.cleaned_data['quantity']
                
                def calcTotal(price, quantity):
                    total = price * quantity
                    return total

                finished_purchase_form.total = calcTotal(price, quantity)
                finished_purchase_form.EID = request.user
                # finished_purchase_form.QID = saved_quote

                saved_purchase = finished_purchase_form.save()

            finished_quote_form.OID = finished_purchase_form
            saved_quote = finished_quote_form.save()

            return HttpResponseRedirect('/')
            
    else:
        purchase_form = PurchaseOrderForm()
        quote_form = QuoteForm()
    return render(request, 'main/order.html', {'purchase_form': purchase_form, 'quote_form': quote_form})


@login_required
def contract(request):
    contracts = Contract.objects.all()
    return render(request, 'main/contract.html')