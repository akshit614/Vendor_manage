from rest_framework import viewsets, status
from .models import Vendors,PurchaseOrders,HistoricalPerformance
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import VendorsSerializers,PurchaseOrdersSerializers,HistoricalPerformanceSerializers



# Create your views here.



class VendorViewSet(viewsets.ModelViewSet):
    # Applying Token based authentication 
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Vendors.objects.all()
    serializer_class = VendorsSerializers

    
    def perform_update(self, serializer):
        instance = serializer.save()
        instance.calculate_performance_metrics()


    @action(detail=True,methods=['get'])
    # Function to get all orders of specific vendor
    def orders(self, request, pk=None):
        try:
            vendor = Vendors.objects.get(pk=pk)
            orders = PurchaseOrders.objects.filter(vendor=vendor)      
            orders_serializers = PurchaseOrdersSerializers(orders,many=True,context={'request':request})
            return Response(orders_serializers.data)
        except Exception as e:
            print(e)
            return Response({
                    'message': 'Vendor does not exist !!'
                })


    @action(detail=True,methods=['get'])
    # Function to get performance metrics of any vendor
    def performance(self, request, pk=None):
        vendor = self.get_object()
        
        performance_metrics = {
            'on_time_delivery_rate': vendor.on_time_delivery_rate,
            'quality_rating_avg': vendor.quality_rating_avg,
            'average_response_time': vendor.average_response_time,
            'fulfillment_rate': vendor.fulfillment_rate,
        }
        return Response(performance_metrics)
    
   
        

class PurchaseOrdersViewSet(viewsets.ModelViewSet):

    # Applying Token based authentication 
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = PurchaseOrders.objects.all()
    serializer_class = PurchaseOrdersSerializers


    @action(detail=True,methods=['post'])
    def acknowledge(self, request, pk=None):
        try:
            po_instance = self.get_object()
            
            # Check if the PurchaseOrder has a valid vendor relationship
            if po_instance.vendor:
                vendor = po_instance.vendor
                vendor.calculate_performance_metrics()
                return Response({'detail': 'Purchase order acknowledged successfully.'}, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'Purchase order does not have a valid vendor.'}, status=status.HTTP_400_BAD_REQUEST)
        
        except PurchaseOrders.DoesNotExist:
            return Response({'detail': 'Purchase order not found.'}, status=status.HTTP_404_NOT_FOUND)




class HistoricalPerformanceViewSet(viewsets.ModelViewSet):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializers
