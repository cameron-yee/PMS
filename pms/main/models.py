from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.

class Quote(models.Model):
    QID = models.AutoField(primary_key=True)
    OID = models.ForeignKey('OrderDetail', on_delete=models.CASCADE, related_name='+')
    QLink = models.TextField(max_length=1000)
    QPrice = models.FloatField()
    Supplier = models.CharField(max_length=30)

class Contract(models.Model):
    CID = models.AutoField(primary_key=True)
    CName = models.CharField(max_length=30)
    CBudget = models.IntegerField()
    CStart = models.DateField()
    CEnd = models.DateField(null=True)

class OrderDetail(models.Model):
    OID = models.AutoField(primary_key=True)
    EID = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    CID = models.ForeignKey(Contract, on_delete=models.CASCADE)
    #null allows blank entry to be stored as null, blank allows the form to be saved without QID
    QID = models.ForeignKey(Quote, on_delete=models.CASCADE, null=True, blank=True)
    productName = models.CharField(max_length=25)
    productDescription = models.CharField(max_length=200)
    addressLine1 = models.CharField(max_length=40)
    addressLine2 = models.CharField(max_length=40, null=True, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=30)
    zipCode = models.CharField(max_length=10)
    quantity = models.IntegerField()
    total = models.FloatField()
    orderDate = models.DateField(default=timezone.now)
    dateApproved = models.DateField(null=True, blank=True)
    dateReceived = models.DateField(null=True, blank=True)