from django.contrib import admin
from .models import OrderDetail, Contract, Quote

class TaskAdmin(admin.ModelAdmin):
    list_display = ['CName', 'CBudget', 'CStart', 'CEnd']
admin.site.register(OrderDetail)
admin.site.register(Contract, TaskAdmin)
admin.site.register(Quote)
