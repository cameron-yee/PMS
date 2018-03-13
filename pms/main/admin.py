from django.contrib import admin
from .models import OrderDetail, Contract, Quote

admin.site.register(OrderDetail)
admin.site.register(Contract)
admin.site.register(Quote)
