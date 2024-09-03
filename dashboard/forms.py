from django import forms

from blogs.models import Blog, Category

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'category', 'feature_image', 'short_description', 'blog_body', 'status', 'is_featured')


