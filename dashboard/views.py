from django.shortcuts import get_object_or_404, redirect, render

from blogs.models import Blog, Category
from dashboard.forms import CategoriaForm, PostForm
from django.template.defaultfilters import slugify

# Create your views here.

def categoria(request):
    

    
    return render(request, 'dashboard/categoria/categorias.html')



def agregar_categoria(request):
    
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categorias')
        
    form = CategoriaForm()
    
    context = {
        'form': form,
    }
    
    return render(request, 'dashboard/categoria/agregar_categoria.html', context)



def editar_categoria(request,pk):
    
    categoria = get_object_or_404(Category, pk=pk)
    
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categorias')
    
    form = CategoriaForm(instance=categoria)
    context = {
        'form': form,
        'categoria': categoria,
    }
    
    return render(request, 'dashboard/categoria/editar_categoria.html', context)


def eliminar_categoria(request, pk):
    
    categoria = get_object_or_404(Category, pk=pk)
    categoria.delete()
    return redirect('categorias')


def posts(request):
    posts = Blog.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'dashboard/posts/posts.html', context)

def agregar_posts(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            #slug
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-' + str(post.id)
            post.save()
            return redirect('posts')
    
    
    form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'dashboard/posts/agregar_posts.html', context)



def editar_posts(request, pk):
    
    post = get_object_or_404(Blog, pk=pk)
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data['title']
            post.slug = slugify(title) + '-' +str(post.id)
            post.save()
            return redirect('posts')
    
    form = PostForm(instance=post)
    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'dashboard/posts/editar_posts.html', context)


def eliminar_posts(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.delete()
    
    return redirect('posts')