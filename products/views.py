from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.views import APIView


# Create your views here.
class CreateProductView(APIView):
    pass

class DetailProductView(RetrieveAPIView):
    pass

class ListProductView(ListAPIView):
    pass

