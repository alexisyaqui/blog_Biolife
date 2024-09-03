from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    #1270.0.0.1/category/1/
    path('categoria/<int:category_id>/', views.post_by_cagegory, name='posts_by_category'),
    path('categoria/<slug:slug>/', views.blogs, name='blogs'),
    path('blogs/search/', views.blogsSearch, name='search')
]