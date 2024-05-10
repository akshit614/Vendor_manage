from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from api.models import PurchaseOrders

@receiver(post_save, sender=PurchaseOrders)
def update_vendor_performance_on_save(sender, instance, created, **kwargs):
    if not created:
        vendor = instance.vendor
        vendor.calculate_performance_metrics()

@receiver(post_delete, sender=PurchaseOrders)
def update_vendor_performance_on_delete(sender, instance, **kwargs):
    vendor = instance.vendor
    vendor.calculate_performance_metrics()
