#from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from tags.serializers import WriteTagserializer, ReadTagserializer
from tags.models import Tags
from django.utils.text import slugify
from django.core.cache import cache
from rest_framework.generics import RetrieveAPIView,ListAPIView,DestroyAPIView
from tags.filters import StandardResultsSetPagination
#This is for generic caching
#from django.views.decorators.cache import cache_page
#from django.utils.decorators import method_decorator
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

class ListTagView(APIView):
    def get(self,request):
        try:
            Queryset = Tags.objects.all()
            #many = True here status that it is not one object. It is many objects. So we have to mention many=True
            response_data = ReadTagserializer(instance=Queryset, many = True).data
            return Response(response_data,status=status.HTTP_200_OK)
        except:
            return Response({"message":"unable to fetch tags list"}, status = status.HTTP_400_BAD_REQUEST)

class DetailTagV2View(RetrieveAPIView):#Here RetrieveAPIView is mentioned because we are fetching one object
    #here retriveapiview takes all the objects and parameter information based on url
    queryset = Tags.objects.all()
    serializer_class = ReadTagserializer
    #Lookup field is responsible for filtering the objects. lets say in URL you mentioned detail/hello
    #then based on slug unformation , the corresponding object is printed in postman window
    lookup_field = "slug"

#The below method decorator is for generic caching
#@method_decorator(cache_page(60*5), name='dispatch')
class ListTagV2View(ListAPIView):#Here ListAPIView is mentioned because we are listing more than 1 object
    #here parameter is not there in url so lookup field is not there, Here we are fetching full json information
    queryset = Tags.objects.all()
    serializer_class = ReadTagserializer
    """
    we can write queryset as below also, tjis is a implementation in method way
    def get_queryset(self):
    queryset = Tags.objecst.all()
    return queryset
    """
    #This is for pagination
    #This part will call filters.py file where pagination details is present
    #HERE in this case filters.py has 3 pages or JSON data printed
    #Goto postman and try printing list view url, you will get 3 JSON data printed and next value link is also provided to check the next 3 values
    pagination_class = StandardResultsSetPagination

class DeleteTagView(APIView):
    #Here for delete we will use delete function. It is not GET or POST
    def delete(self, request, slug):
        try:
            tag_object = Tags.objects.get(slug=slug)
            tag_object.delete()
            return Response({"message",f"Tag deleted with slug {slug}"}, status=status.HTTP_200_OK)
        except Tags.DoesNotExist:
            return Response({"message":"Tag not found"},status=status.HTTP_404_NOT_FOUND)
        except Tags.MultipleObjectReturned:
            return Response({"message":"Multiple tags exist for given slug"},status=status.HTTP_400_BAD_REQUEST)

class DeleteTagV2View(DestroyAPIView):
    #DestroAPI view is helpfull for deleting the object
    queryset = Tags.objects.all()
    #serializer_class = ReadTagserializer
    lookup_field = "slug"