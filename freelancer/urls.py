from django.urls import path

from freelancer import views

urlpatterns = [
    path('', views.get_users, name='Freelancers'),
]
