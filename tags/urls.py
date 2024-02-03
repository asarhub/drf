from django.urls import path, include
from tags.views import CreateTagView, DetailTagView,ListTagView

urlpatterns = [
    path('create/', CreateTagView.as_view(), name='create_tag'),
    path('detail/<str:slug>/', DetailTagView.as_view(), name='detail_tag'),
    path('list/', ListTagView.as_view(), name='list_tag')
]