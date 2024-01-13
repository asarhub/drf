#from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from tags.serializers import WriteTagserializer, ReadTagserializer
from tags.models import Tags
from django.utils.text import slugify
class CreateTagView(APIView):
    def post(self,request):
        #for write operation we use data=request.data(from client side validation)
        serializer = WriteTagserializer(data=request.data)
        if serializer.is_valid():
            name =serializer.validated_data.get('name')
            tag_object =Tags.objects.create(
                name = name,
                slug = slugify(name)
            )
            #Important note
            #For read operatio n we use instance = tag_object
            json_data = ReadTagserializer(instance=tag_object).data
            return Response(json_data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)






# Create your views here.
