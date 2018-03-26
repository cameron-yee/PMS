from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django import forms
from django.contrib.auth.decorators import login_required
from .forms import * 
from django.contrib.auth.models import User
from .models import Contract, Quote, OrderDetail
from datetime import datetime

last_OID = None

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
        quote_form_2 = QuoteForm(request.POST)
        quote_form_3 = QuoteForm(request.POST)
        price = 0
        quantity = 0.0
        saved_quote = 0

        if quote_form.is_valid():
            finished_quote_form = quote_form.save(commit=False)
            price = quote_form.cleaned_data['QPrice']

            if purchase_form.is_valid():
                finished_purchase_form = purchase_form.save(commit=False)

                quantity = purchase_form.cleaned_data['quantity']

                def calcTotal(price, quantity):
                    total = price * quantity
                    return total

                finished_purchase_form.total = calcTotal(price, quantity)
                finished_purchase_form.EID = request.user

                finished_purchase_form.save()
                last_OID = finished_purchase_form.OID

            finished_quote_form.OID = finished_purchase_form
            finished_quote_form.save()

            user_email = request.user.email

            if finished_purchase_form.total < 50:
                current_purchase_form = finished_purchase_form 
                current_quote = finished_quote_form

                def setChosenQuote(current_purchase_form, current_quote):
                    quote = current_quote
                    current_purchase_form.QID = quote
                    current_purchase_form.dateApproved = datetime.now()
                    current_purchase_form.save()

                setChosenQuote(current_purchase_form, current_quote)

                send_mail(
                    'PURCHASE ORDER CONFIRMATION',
                    'Hi {}, you\'re purchase order form has been received.  The order form has been approved with the given quote.\n\nPurchase Management System'.format(request.user.first_name),
                    'yee.camero23@gmail.com', #Make info@system.com email
                    [user_email],
                    fail_silently=False,
                )
            elif finished_purchase_form.total >= 500:
                    request.session['selected_order'] = finished_purchase_form.OID
                    return HttpResponseRedirect('/main/quotes')
            else:
                send_mail(
                    'PURCHASE ORDER CONFIRMATION',
                    'Hi {}, you\'re purchase order form has been received. Management will get back to you after reviewing the quote\n\nPurchase Management System'.format(request.user.first_name),
                    'yee.camero23@gmail.com', #Make info@system.com email
                    [user_email],
                    fail_silently=False,
                )

            return HttpResponseRedirect('/')
            
    else:
        purchase_form = PurchaseOrderForm()
        quote_form = QuoteForm()
    return render(request, 'main/order.html', {'purchase_form': purchase_form, 'quote_form': quote_form})

@login_required
def quote(request):
    selected_order = OrderDetail.objects.get(OID=request.session['selected_order'])
    #MIGHT NEED TO CLOSE SESSIONS

    if request.method == "POST":
        quote_form2 = QuoteForm(request.POST)
        quote_form3 = QuoteForm(request.POST)
        user_email = request.user.email
        if quote_form2.is_valid():
            finished_quote_form2 = quote_form2.save(commit=False)
            finished_quote_form2.OID = selected_order
            saved_quote2 = finished_quote_form2.save()
        
        if quote_form3.is_valid():
            finished_quote_form3 = quote_form3.save(commit=False)
            finished_quote_form3.OID = selected_order
            saved_quote3 = finished_quote_form3.save()

            send_mail(
                'PURCHASE ORDER CONFIRMATION',
                'Hi {}, you\'re purchase order form has been received. Since the order is over $500, it may take longer to review. Management will get back to you after reviewing the provided quotes.\n\nPurchase Management System'.format(request.user.first_name),
                'yee.camero23@gmail.com', #Make info@system.com email
                [user_email],
                fail_silently=False,
            )
        return HttpResponseRedirect('/')
            
    else:
        quote_form2 = QuoteForm()
        quote_form3 = QuoteForm()        
    return render(request, 'main/quotes.html', {'quote_form2': quote_form2, 'quote_form3': quote_form3})
    

@login_required
def contract(request):
    contracts = Contract.objects.all()
    return render(request, 'main/contract.html', {'contracts': contracts})


@login_required
def myorders(request):
    user_id = request.user.id
    myorders = OrderDetail.objects.all() #filter(EID=user_id)
    return render(request, 'main/myorders.html', {'myorders': myorders})
