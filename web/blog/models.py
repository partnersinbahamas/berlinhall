from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField('Title', max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, verbose_name="category-url", unique=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse_lazy('categories', kwargs={ 'slug': self['slug'] })
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['pk']

class Tag(models.Model):
    name = models.CharField('Title', max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, verbose_name="tag-url", unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['pk']

class Post(models.Model):
    title = models.CharField('Title', max_length=50)
    slug = models.CharField(verbose_name='post-url', max_length=50)
    content = models.TextField('Content', blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, null=True, related_name='posts_author')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts_category', null=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts_tag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField('Image', upload_to='images/%Y/%m/%d', blank=True)
    views = models.IntegerField('Views', default=0)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse_lazy('posts', kwargs={ 'slug': self['slug'] })
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created_at']