from rest_framework import serializers
from tags.models import Tags

#Serializer is used to convert orm data into json
#read operation from the database
class ReadTagserializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d/%m/%y")
    class Meta:
        model = Tags
        fields = ['id', 'name', 'slug', 'created_at','updated_at']

#Write operation into the database
#Used for data validation and tag creation
class WriteTagserializer(serializers.ModelSerializer):
   #created_at = serializers.DateTimeField(format="%d/%m/%y")
    class Meta:
        model = Tags
        fields = ['name']