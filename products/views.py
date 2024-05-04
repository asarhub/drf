from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from authentication.permissions import IsAdminUser
from products.models import Products
from products.serializers import WriteProductSerializer,ReadProductSerializer
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.utils.text import slugify
from tags.filters import StandardResultsSetPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class CreateProductView(APIView):
    #Only admin is permitted to add the products
    permission_classes = (IsAdminUser, )
    def post(self,request):
        serializer = WriteProductSerializer(data=request.data)
        print(serializer)
        print("<<<<<<")
        if serializer.is_valid():
            product = Products.objects.create(
                name=serializer.validated_data.get('name'),
                slug=slugify(serializer.validated_data.get('name')),
                price=serializer.validated_data.get('price'),
                quantity=serializer.validated_data.get('quantity'),
                description=serializer.validated_data.get('description')
            )
            #print(product)
            product.tags.set(serializer.validated_data.get('tags'))
            response_data = ReadProductSerializer(instance=product).data
            return Response(response_data,status=HTTP_200_OK)
            #return Response(status=HTTP_200_OK)
        else:
            print("&&&&&&&&&&&&")
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class DetailProductView(RetrieveAPIView):
    #Here based on id, we can print the values present in the database
    queryset = Products.objects.all()
    serializer_class = ReadProductSerializer
    lookup_field = 'id'

class ListProductView(ListAPIView):
    #queryset parameter will be taken by ReadProductSerializer directly. This fucntionality is given only in ListAPIView or RetrieveAPIView
    queryset = Products.objects.all()
    serializer_class = ReadProductSerializer
    pagination_class = StandardResultsSetPagination
    authentication_classes = []
    permission_classes = []
    filter_backends = [filters.OrderingFilter,filters.SearchFilter,DjangoFilterBackend]
    Ordering_fields = ['id','created_at']
    #we can print the data in reverse way based on id using the code below,(If WE Dont write any query params)
    ordering = ["-id"]
    #open it in mozilla firefox, you will get everything-127.0.0.1:8000/products/list
    search_fields = ["^name"]
    filterset_fields = ["id","price","tags"]

