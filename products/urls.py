from django.urls import path
from products.views import CreateProductView,ListProductView,DetailProductView
urlpatterns = [
    path('create/',CreateProductView.as_view(),name="Create_product"),
    path('list/',ListProductView.as_view(),name="List_product"),
    path('detail/<int:id>/',DetailProductView.as_view(),name="detail_product")
]