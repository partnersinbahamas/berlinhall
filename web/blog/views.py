from django.shortcuts import render

# Create your views here.

def blog_home(request):
    return render(request, 'blog/blog.html')

def with_categories(request, slug):
    return render(request, 'blog/blog.html')
