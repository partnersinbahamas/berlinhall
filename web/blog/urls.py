from django.urls import path
from .views import blog_home, with_categories

urlpatterns = [
    path('', blog_home, name="home"),
    path('category/<str:slug>', with_categories, name="category")
]