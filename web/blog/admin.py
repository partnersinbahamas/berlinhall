from django.contrib import admin
from .models import Category, Tag, Post

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    # generate slug field using model name
    prepopulated_fields = {"slug": ["name"]}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
