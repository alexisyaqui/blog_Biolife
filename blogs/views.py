from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from blogs.models import Blog, Category
from django.db.models import Q

# Create your views here.
def home(request):
    posts = Blog.objects.filter(is_featured=True).order_by('-update_at')
    
    context = {
        'featured_posts': posts # 
    }
    return render(request, 'index.html', context)


def post_by_cagegory(request, category_id):
    posts = Blog.objects.filter(status='Published', category=category_id)
    #category = get_object_or_404(Category, pk=category_id)
    
    try:
        category = Category.objects.get(pk=category_id)
    except:
        return redirect('home')
    
    context = {
        'posts': posts,
        'category': category,
    }
    
    return render(request, 'posts_by_category.html', context)


def blogs(request, slug):
    
    single_blog = get_object_or_404(Blog, slug=slug)
    
    context = {
        'single_blog': single_blog
    }
    
    return render(request, 'blog.html', context)



def blogsSearch(request):
    keyword = request.GET.get('keyword')
    
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword))
    
    context = {
        'blogs': blogs,
        'keyword': keyword
    }
    
    return render(request, 'search.html', context)
    