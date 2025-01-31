from django.urls import path
from .views import with_categories, Home

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('category/<str:slug>', with_categories, name="category"),
    # temporary url
    path('posts/<str:slug>', Home.as_view(), name="posts")
] 