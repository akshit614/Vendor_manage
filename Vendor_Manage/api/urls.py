from django.contrib import admin
from django.urls import path,include
from api.views import VendorViewSet,PurchaseOrdersViewSet,HistoricalPerformanceViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'vendors', VendorViewSet)
router.register(r'purchase_orders', PurchaseOrdersViewSet)
router.register(r'performance', HistoricalPerformanceViewSet)
# router.register(r'purchase_orders', PurchaseOrdersViewSet, basename='purchase_orders')


urlpatterns = [
    path('', include(router.urls)),

]
