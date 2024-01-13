from rest_framework import serializers
from tags.models import Tags
class Tagserializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d/%m/%y")
    class Meta:
        model = Tags
        fields = ['id', 'name', 'slug', 'created_at','updated_at']