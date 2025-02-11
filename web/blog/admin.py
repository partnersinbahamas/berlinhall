from django import forms
from django.contrib import admin
from .models import Category, Tag, Post, Comment
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    # generate slug field using model name
    prepopulated_fields = {"slug": ["name"]}

    fields = ('name', 'slug')
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'slug')
    search_fields = ('id', 'name', 'slug')
    list_filter = ('id', 'slug', 'name')

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}

    fields = ('name', 'slug')
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'slug')
    search_fields = ('id', 'name', 'slug')
    list_filter = ('id', 'slug', 'name')

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    save_on_top = True
    prepopulated_fields = {"slug": ["title"]}

    list_display = ('id', 'slug', 'author', 'category', 'created_at', 'updated_at', 'render_image', 'views')
    list_display_links = ('id', 'slug', 'author')
    readonly_fields = ('created_at', 'updated_at', 'views')
    search_fields = ('title', 'content', 'slug')
    list_filter = ('title', 'author', 'category', 'created_at', 'updated_at', 'views') 

    def render_image(self, obj):
        if obj.image:
            # mark_safe makes our image not as 'escaped'
            return mark_safe(f'<img src="{obj.image.url}" width="40" height="40">')
    
    # to see right name in admin instead of 'render image'
    render_image.short_description = "Image"

class CommentAdmin(admin.ModelAdmin):
    fields = ('author', 'content', 'created_at')
    list_display =  ('author', 'content', 'created_at')
    list_display_links = ('author', 'content')
    search_fields = ('content',)
    list_filter = ('author', 'content', 'created_at')
    readonly_fields = ('created_at',)

admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
