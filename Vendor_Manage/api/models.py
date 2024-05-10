from django.db import models
from django.db.models import  Avg, ExpressionWrapper, F, DurationField
from datetime import timedelta
from rest_framework.views import APIView

# Create your models here.

# Vendors model

class Vendors(models.Model):
    name = models.CharField(max_length=50)
    contact_details = models.TextField()
    address = models.TextField(max_length=255)
    vendor_code = models.CharField(max_length=20, unique=True)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()
    
    # Function to calculate the performance metrtics
    def calculate_performance_metrics(self):
        
        # Calculate on-time delivery rate
        completed_pos = self.purchaseorders_set.filter(status='completed')
        total_completed_pos = completed_pos.count()
        if total_completed_pos > 0:
            on_time_pos = completed_pos.filter(delivery_date__lte=models.F('acknowledgment_date'))
            self.on_time_delivery_rate = (on_time_pos.count() / total_completed_pos) * 100
        else:
            self.on_time_delivery_rate = 0.0
        
        # Calculate quality rating average
        completed_pos_with_rating = completed_pos.exclude(quality_rating__isnull=True)
        if completed_pos_with_rating.exists():
            self.quality_rating_avg = completed_pos_with_rating.aggregate(avg_rating=Avg('quality_rating'))['avg_rating']
        else:
            self.quality_rating_avg = 0.0
        
        
        # Calculate average response time 
        response_times = completed_pos.filter(acknowledgment_date__isnull=False).annotate(
            response_time=ExpressionWrapper(F('acknowledgment_date') - F('issue_date'), output_field=DurationField())
        ).aggregate(avg_response_time=Avg('response_time'))

        # Extract average response time in seconds
        avg_response_time_seconds = response_times['avg_response_time'].total_seconds() if response_times['avg_response_time'] else 0.0
        self.average_response_time = avg_response_time_seconds/60
          
        # Calculate fulfillment rate
        successful_pos = completed_pos.filter(issue_date__isnull=False)
        total_pos_count = self.purchaseorders_set.count()
        if total_pos_count > 0:
            self.fulfillment_rate = (successful_pos.count() / total_pos_count) * 100
        else:
            self.fulfillment_rate = 0.0
        
        self.save()

    def __str__(self):
        return self.name
       # return f"{self.name }  {self.address}  ({self.vendor_code})"
    
    

# PurchaseOrders model

class PurchaseOrders(models.Model):
    po_number = models.CharField(max_length=20, unique=True)
    vendor = models.ForeignKey(Vendors, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50)
    quality_rating = models.FloatField(null=True,blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True,blank=True)

    
    # def __str__(self):
    #     return f"PO {self.po_number} ({self.vendor.name}

# HistoricalPerformance model
class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendors, on_delete=models.CASCADE, related_name='historical_performances')
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()




