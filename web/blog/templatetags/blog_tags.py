from django import template

register = template.Library()
from ..models import Category

@register.inclusion_tag('inc/_nav.html')
def show_categories():
    categories = Category.objects.all()

    return { 'categories': categories }

