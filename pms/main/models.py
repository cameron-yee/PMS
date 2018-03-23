from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.conf import settings


# Create your models here.

class Quote(models.Model):
    QID = models.AutoField(primary_key=True, verbose_name= 'quote ID')
    OID = models.ForeignKey('OrderDetail', on_delete=models.CASCADE, related_name='+', verbose_name= 'order ID')
    QLink = models.CharField(max_length=1000, verbose_name= 'website Link')
    QPrice = models.FloatField(verbose_name= 'item Price')
    Supplier = models.CharField(max_length=30)
    def __str__(self):
        return 'QID: {} {}'.format(self.OID, self.Supplier)

class Contract(models.Model):
    CID = models.AutoField(primary_key=True, verbose_name= 'contract ID')
    CName = models.CharField(max_length=30, verbose_name= 'contract Name')
    CBudget = models.IntegerField(verbose_name= 'budget')
    CStart = models.DateField(verbose_name= 'contract Start Date')
    CEnd = models.DateField(null=True, verbose_name= 'contract End Date')
    def __str__(self):
        return '{}'.format(self.CName)

class OrderDetail(models.Model):
    OID = models.AutoField(primary_key=True, verbose_name = 'order ID')
    EID = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, verbose_name = 'employee ID')
    CID = models.ForeignKey(Contract, on_delete=models.CASCADE)
    #null allows blank entry to be stored as null, blank allows the form to be saved without QID
    QID = models.ForeignKey(Quote, on_delete=models.CASCADE, null=True, blank=True, verbose_name= 'quoteID')
    productName = models.CharField(max_length=25, verbose_name= 'item Name')
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
    isPending = models.BooleanField(default=True, verbose_name= 'Pending')
    isDenied = models.BooleanField(default=False, verbose_name= 'Denied')
    isApproved = models.BooleanField(default=False, verbose_name= 'Approved')
    def __str__(self):
        return '{}'.format(self.OID)