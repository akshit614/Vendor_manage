from django.contrib import admin
from api.models import Vendors,PurchaseOrders,HistoricalPerformance

# Register your models here.

class VendorAdmin(admin.ModelAdmin):
    list_display = ('name','address','vendor_code')

class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('po_number','vendor','items','quantity')


admin.site.register(Vendors,VendorAdmin)
admin.site.register(PurchaseOrders,PurchaseOrderAdmin)
admin.site.register(HistoricalPerformance)
