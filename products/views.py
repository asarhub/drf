from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from authentication.permissions import IsAdminUser
from products.models import Products
from products.serializers import WriteProductSerializer
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.utils.text import slugify

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
            product.tags.set(serializer.validated_data.get('tags'))
            return Response(status=HTTP_200_OK)
        else:
            print("&&&&&&&&&&&&")
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class DetailProductView(RetrieveAPIView):
    pass

class ListProductView(ListAPIView):
    pass

