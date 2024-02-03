from django.urls import path, include
from tags.views import CreateTagView, DetailTagView,ListTagView,DetailTagV2View, ListTagV2View,DeleteTagView,DeleteTagV2View


urlpatterns = [
    path('create/', CreateTagView.as_view(), name='create_tag'),
    path('detail/<str:slug>/', DetailTagView.as_view(), name='detail_tag'),#This is for API view
    path('detail/v2/<str:slug>/', DetailTagV2View.as_view(), name='detail_tag_v2'),#This is for Generic view
    path('delete/<str:slug>/', DeleteTagView.as_view(), name='delete_tag'),
    path('delete/v2/<str:slug>/', DeleteTagV2View.as_view(), name='delete_tag_v2'),
    path('list/', ListTagView.as_view(), name='list_tag'),#This is for API
    path('list/v2/', ListTagV2View.as_view(), name='list_tag_v2')#This is for Generic
]