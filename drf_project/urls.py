from django.urls import path, include




# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('tags/', include('tags.urls')),
    path('authentication/', include('authentication.urls')),
    path('products/',include('products.urls')),
    path('Orders/',include('orders.urls'))
]