from django.contrib import admin
from .models import OrderDetail, Contract, Quote

class ContractAdmin(admin.ModelAdmin):
    list_display = ['CName', 'CBudget', 'CStart', 'CEnd']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['OID', 'EID', 'CID', 'productName', 'total', 'orderDate', 'QID']

class QuoteAdmin(admin.ModelAdmin):
    list_display = ['OID', 'QPrice', 'Supplier']

admin.site.register(OrderDetail, OrderAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Quote, QuoteAdmin)
