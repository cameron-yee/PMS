from django import forms
from django.forms import ModelForm
from . import models

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


class PurchaseOrderForm(ModelForm):
    class Meta: 
        model = models.OrderDetail
        fields = ['orderDate', 'CID', 'productName', 'productDescription', 'deliveryAddress','quantity']

    def __init__(self, *args, **kwargs):
        super(PurchaseOrderForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance:
            self.fields['orderDate'].widget.attrs['readonly'] = True

class QuoteForm(ModelForm):
    class Meta: 
        model = models.Quote
        fields = ['QLink', 'Qprice', 'Supplier']