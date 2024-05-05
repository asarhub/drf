from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from authentication.permissions import IsAdminUser
from products.serializers import WriteProductSerializer,ReadProductSerializer
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.utils.text import slugify
from tags.filters import StandardResultsSetPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from products.models import Products

# Create your views here.
class CreateOrderView(APIView):

    def compute_total_amount(self, orders):
        total_amount = 0
        for product_id, qty in orders.items():
            try:
                product_id=int(product_id)
                product = Products.objects.get(pk=product_id)
                qty = min(product.quantity,int(qty))
                total_amount+=product.price * qty
            except Products.DoesNotExist:
                pass
        return total_amount
    def post(self, request):
        orders = request.data.get('orders')
        payment_mode = request.data.get('payment_mode')
        payment_status = request.data.get('payment_status')
        user_id = request.user
        total_amount = self.compute_total_amount(orders)
        return Response(total_amount)
class OrderDetailView(RetrieveAPIView):
    pass
class OrderListView(ListAPIView):
    pass


