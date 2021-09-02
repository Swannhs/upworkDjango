from django.urls import path

from feed import views

urlpatterns = [
    path('posts/', views.get_posts, name='Posts'),
]
