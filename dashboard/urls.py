from django.urls import path 
from . import views 

urlpatterns = [
    path('categoria/', views.categoria, name='categorias'),
    path('categoria/agregar/', views.agregar_categoria, name='agregar_categoria'),
    path('categoria/editar/<int:pk>/', views.editar_categoria, name='editar_categoria'),
    path('categoria/eliminar/<int:pk>/', views.eliminar_categoria, name='eliminar_categoria'),
    
    
    #posts 
    path('posts/', views.posts, name='posts'),
    path('posts/agregar_posts/', views.agregar_posts, name='agregar_posts'),
    path('posts/editar/<int:pk>/', views.editar_posts, name='editar_posts'),
    path('posts/eliminar/<int:pk>/', views.eliminar_posts, name='eliminar_posts'),

]