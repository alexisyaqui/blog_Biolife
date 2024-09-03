from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    categoria_name = models.CharField(max_length=50, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        
    def __str__(self):
        return f'{self.categoria_name}'
    
STATUS_CHOICES = (
    ('Draft', 'Draft'),
    ('Published', 'Published'),
)
    
class Blog(models.Model):
    title = models.CharField(max_length=100)#
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)#
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    feature_image = models.ImageField(upload_to='uploads/%Y/%m/%d')#
    short_description = models.TextField(max_length=500)#
    blog_body = models.TextField(max_length=2000)#
    status = models.TextField(max_length=20, choices=STATUS_CHOICES, default="Draft")
    is_featured = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        
        
    def __str__(self):
        return f'{self.title} {self.author}'
    