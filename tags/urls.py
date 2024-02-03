from django.urls import path, include
from tags.views import CreateTagView, DetailTagView

urlpatterns = [
    path('create/', CreateTagView.as_view(), name='create_tag'),
    path('detail/<str:slug>/', DetailTagView.as_view(), name='detail_tag')
]