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
        #Use case 1
        #print(request+"Not found bhai")
        serializer = WriteTagserializer(data=request.data)
        if serializer.is_valid():
            name =serializer.validated_data.get('name')
            tag_object =Tags.objects.create(
                name = name,
                slug = slugify(name)
            )
            #Important note
            #For read operatio n we use instance = tag_object
            #Use case 2
            json_data = ReadTagserializer(instance=tag_object).data
            return Response(json_data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
class DetailTagView(APIView):
    #We will get the name of object based on slug information provided
    def get(self, request, slug):
        try:
            tag_object = Tags.objects.get(slug=slug)
            response_data = ReadTagserializer(instance = tag_object).data
            return Response(response_data, status=status.HTTP_200_OK)
        except Tags.DoesNotExist:
            return Response({"message":"Tag not found"},status=status.HTTP_404_NOT_FOUND)
        except Tags.MultipleObjectReturned:
            return Response({"message":"Multiple tags exist for given slug"},status=status.HTTP_400_BAD_REQUEST)


