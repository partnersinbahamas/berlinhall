from django.urls import path
from .views import Home, PostCategories, PostDetail

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('category/<str:slug>', PostCategories.as_view(), name="category"),
    path('posts/<str:slug>', PostDetail.as_view(), name="posts"),
] 