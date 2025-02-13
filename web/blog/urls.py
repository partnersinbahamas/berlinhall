from django.urls import path
from .views import Home, PostCategories, PostDetail, PostTags, SearchPost

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('category/<str:slug>', PostCategories.as_view(), name="category"),
    path('tags/<str:slug>', PostTags.as_view(), name="tags"),
    path('posts/<str:slug>', PostDetail.as_view(), name="posts"),
    path('search', SearchPost.as_view(), name="search"),
] 