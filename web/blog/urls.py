from django.urls import path
from .views import Home, PostCategories

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('category/<str:slug>', PostCategories.as_view(), name="category"),
    # temporary url
    path('posts/<str:slug>', Home.as_view(), name="posts")
] 