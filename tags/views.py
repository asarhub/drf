#from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from tags.serializers import WriteTagserializer, ReadTagserializer
from tags.models import Tags
from django.utils.text import slugify
from django.core.cache import cache
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
    #You can check it in postman where URL has {{LOCAL_HOST}}/tags/detail/slug_name
    def get(self, request, slug):
        try:
            #This code is for caching,currently it is not working
            #Enable all the code present below to check whether cache is working or not. When you are viewing detials for the first time it is cached next time it will come from cache
            #cache_key = f"tags-{slug}"
            #cached_data = cache.get(cache_key)
            #if cached_data is not None:
                #print("coming from cache")
                #return Response(cached_data,status=status.HTTP_200_OK)
            tag_object = Tags.objects.get(slug=slug)
            response_data = ReadTagserializer(instance = tag_object).data
            #print("Generating and caching the data")
            #timeout is the time till when this data will be cached. It is in seconds format
            #cache.set(cache_key,response_data,timeout=10)
            return Response(response_data, status=status.HTTP_200_OK)
        except Tags.DoesNotExist:
            return Response({"message":"Tag not found"},status=status.HTTP_404_NOT_FOUND)
        except Tags.MultipleObjectReturned:
            return Response({"message":"Multiple tags exist for given slug"},status=status.HTTP_400_BAD_REQUEST)


