from django.urls import path
from orders.views import CreateOrderView,OrderListView,OrderDetailView
urlpatterns = [
    path('create/',CreateOrderView.as_view(),name="Create_Orders"),
    path('list/',OrderListView.as_view(),name="List_product"),
    path('detail/<int:id>/',OrderDetailView.as_view(),name="detail_product")
]