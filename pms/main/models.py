from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.

class Quote(models.Model):
    QID = models.AutoField(primary_key=True, verbose_name= 'quote ID')
    OID = models.ForeignKey('OrderDetail', on_delete=models.CASCADE, related_name='+', verbose_name= 'order ID')
    QLink = models.TextField(max_length=1000, verbose_name= 'link')
    QPrice = models.FloatField(verbose_name= 'price')
    Supplier = models.CharField(max_length=30)

class Contract(models.Model):
    CID = models.AutoField(primary_key=True, verbose_name= 'contract ID')
    CName = models.CharField(max_length=30, verbose_name= 'contract Name')
    CBudget = models.IntegerField(verbose_name= 'budget')
    CStart = models.DateField(verbose_name= 'contract Start Date')
    CEnd = models.DateField(null=True, verbose_name= 'contract End Date')

class OrderDetail(models.Model):
    OID = models.AutoField(primary_key=True, verbose_name = 'order ID')
    EID = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, verbose_name = 'employee ID')
    CID = models.ForeignKey(Contract, on_delete=models.CASCADE, verbose_name = 'Contract ID')
    #null allows blank entry to be stored as null, blank allows the form to be saved without QID
    QID = models.ForeignKey(Quote, on_delete=models.CASCADE, null=True, blank=True, verbose_name= 'quoteID')
    productName = models.CharField(max_length=25, verbose_name= 'product Name')
    productDescription = models.CharField(max_length=200, verbose_name= 'description')
    addressLine1 = models.CharField(max_length=40)
    addressLine2 = models.CharField(max_length=40, null=True, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=30)
    zipCode = models.CharField(max_length=10, verbose_name= 'zip Code')
    quantity = models.IntegerField()
    total = models.FloatField(verbose_name= 'order Total')
    orderDate = models.DateField(default=timezone.now, verbose_name= 'date Requested')
    dateApproved = models.DateField(null=True, blank=True, verbose_name= 'date Approved')
    dateReceived = models.DateField(null=True, blank=True, verbose_name= 'date Received')