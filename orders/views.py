from django.db import transaction
from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from authentication.permissions import IsAdminUser
from orders.models import OrderItems, Order
from products.serializers import WriteProductSerializer,ReadProductSerializer
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.utils.text import slugify
from tags.filters import StandardResultsSetPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from products.models import Products

# Create your views here.
class CreateOrderView(APIView):
    def post(self, request):
        orders = request.data.get('orders')
        payment_mode = request.data.get('payment_mode')
        payment_status = request.data.get('payment_status')
        user_id = request.user.id
        #Transaction.atomic helps for bringing Automicity in the projects or code logic . Here transaction or orderitems is happening so it suits
        with transaction.atomic():
            order = Order.objects.create(
                user_id=user_id,
                payment_mode=payment_mode,
                payment_status=payment_status,
                payment_amount=0 #Doing this to 0. Initially we set the payment amount as 0 to avaoid incurrect values will be updated into the database
            )
            total_amount =0
            #Once order is created we will create the orderItems , once the orderItem is created we can ensure that transaction is completed and succesfull so that we can update it into the database
            for product_id, qty in orders.items():
                 product_id = int(product_id)
                 product = Products.objects.get(pk=product_id)
                 qty = min(product.quantity, int(qty))
                 total_amount += product.price * qty
                 OrderItems.objects.create(
                        product_id=product_id,
                        order_id = order.id,
                     #This is the price at the time or order, so we can add any discount value as well here
                        price=product.price,
                        quantity=qty
                    )
            #Once the order amount is calculated, we will update it into the order table or database
            order.payment_amount=total_amount
            order.save()
        return Response(total_amount)

class OrderDetailView(RetrieveAPIView):
    pass
class OrderListView(ListAPIView):
    pass


