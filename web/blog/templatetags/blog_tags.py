from django import template

register = template.Library()
from ..models import Category, Post

@register.inclusion_tag('inc/_nav.html')
def show_categories():
    categories = Category.objects.all()

    return { 'categories': categories }

@register.simple_tag()
def get_latest_post():
    return Post.objects.latest('updated_at')

@register.simple_tag()
def get_latest_category_post(category_slug):

    return Post.objects.filter(category__slug=category_slug).latest('updated_at')

@register.simple_tag()
def posts_by_category(category_slug):
    return Post.objects.filter(category__slug=category_slug)

