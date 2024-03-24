from rest_framework import serializers
from products.models import Products

class WriteProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['name', 'description','price','quantity','tags']

class ReadProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id','name', 'description','price','quantity']