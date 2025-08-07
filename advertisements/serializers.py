from rest_framework import serializers
from .models import Advertisement


class AdvertisementSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    
    class Meta:
        model = Advertisement
        fields = '__all__'
        
    def update(self, instance, validated_data):
        # Handle image update - only update if new image is provided
        if 'image' not in validated_data or validated_data['image'] is None:
            validated_data.pop('image', None)
        return super().update(instance, validated_data)