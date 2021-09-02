from django.urls import path

from feed import views

urlpatterns = [
    path('posts/', views.get_posts, name='Posts'),
    path('post/<str:id>', views.get_post, name='Post'),
    path('create/', views.make_post, name='Create'),
]
