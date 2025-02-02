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

