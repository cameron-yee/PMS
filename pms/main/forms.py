from django import forms
from django.forms import ModelForm
from . import models
from .models import OrderDetail, Contract

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

class MyModelChoiceField(forms.ModelChoiceField): #gets the Contract name for the ChoiceFields in the form
    def label_from_instance(self, obj):
        return obj.CName

class PurchaseOrderForm(ModelForm):
    CID = MyModelChoiceField(queryset=Contract.objects.all())
    class Meta: 
        model = models.OrderDetail
        fields = ['orderDate', 'CID', 'productName', 'productDescription', 'addressLine1', 'addressLine2', 'city', 'state', 'zipCode','quantity']

    def __init__(self, *args, **kwargs):
        super(PurchaseOrderForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance:
            self.fields['orderDate'].widget.attrs['readonly'] = True
            
class QuoteForm(ModelForm):
    class Meta:
        model = models.Quote
        fields = ('Supplier', 'QPrice', 'QLink')
