# vendors/serializers.py

from rest_framework import serializers
from api.models import Vendors,PurchaseOrders,HistoricalPerformance
from django.contrib.auth.models import User


class VendorsSerializers(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Vendors
        fields = '__all__'

class PurchaseOrdersSerializers(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = PurchaseOrders
        fields = '__all__'


class HistoricalPerformanceSerializers(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = HistoricalPerformance
        fields = '__all__'

