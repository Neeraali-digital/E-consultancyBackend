from rest_framework import serializers
from .models import Payment
from applications.serializers import ApplicationSerializer

class PaymentSerializer(serializers.ModelSerializer):
    application = ApplicationSerializer(read_only=True)
    application_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Payment
        fields = ['id', 'application', 'application_id', 'amount', 'payment_date', 'payment_method', 'transaction_id', 'status', 'created_at', 'updated_at']
        read_only_fields = ['id', 'payment_date', 'created_at', 'updated_at']