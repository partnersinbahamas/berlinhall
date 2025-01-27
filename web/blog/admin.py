from django import forms
from django.contrib import admin
from .models import Category, Tag, Post
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    # generate slug field using model name
    prepopulated_fields = {"slug": ["name"]}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name"]}

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    prepopulated_fields = {"slug": ["title"]}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
