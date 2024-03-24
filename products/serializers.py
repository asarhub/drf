from rest_framework import serializers
from products.models import Products
from tags.serializers import ReadTagserializer

class WriteProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['name', 'description','price','quantity','tags']

class ReadProductSerializer(serializers.ModelSerializer):
    """
        method_name = 'get_tags' is not necessary in serializers.SerializerMethodField(method_name='get_tags') stated above
        if we dint specify it, be default it will take get_<field_name>, where <field_name> is 'tags'.
        where 'tags' is the LHS of the tags = serializers.SerializerMethodField()
        The condition is if we dint specify the method_name then all the names should be tags only(In 3 places of above code). Please check in notes!!!
        """
    tags = serializers.SerializerMethodField(method_name='get_tags')
    class Meta:
        model = Products
        fields = ['id','name', 'description','price','quantity','tags']
    def get_tags(self,products):
        qeuryset = products.tags.all()
        return ReadTagserializer(qeuryset, many=True).data
