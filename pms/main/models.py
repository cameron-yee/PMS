from django.db import models

# Create your models here.

class Quote(models.Model):
    QID = models.AutoField(primary_key=True)
    OID = models.ForeignKey('OrderDetail', on_delete=models.CASCADE, related_name='+')
    QLink = models.TextField(max_length=2000)
    QPrice = models.FloatField()
    Supplier = models.CharField(max_length=30)

class Contract(models.Model):
    CID = models.AutoField(primary_key=True)
    CName = models.TextField(max_length=50)
    CBudget = models.IntegerField()
    CStart = models.DateField()
    CEnd = models.DateField(null=True)

class OrderDetail(models.Model):
    OID = models.AutoField(primary_key=True)
    EID = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    CID = models.ForeignKey(Contract, on_delete=models.CASCADE)
    #null allows blank entry to be stored as null, blank allows the form to be saved without QID
    QID = models.ForeignKey(Quote, on_delete=models.CASCADE, null=True, blank=True)
    productName = models.CharField(max_length=20)
    productDescription = models.TextField(max_length=200)
    deliveryAddress = models.TextField(max_length=200)
    quantity = models.IntegerField()
    total = models.FloatField()
    orderDate = models.DateField()
    dateApproved = models.DateField()
    dateReceived = models.DateField()






