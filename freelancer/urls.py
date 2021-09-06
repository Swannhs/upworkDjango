from django.urls import path

from freelancer import views
from freelancer.serializers import RegisterAPI
from freelancer.views import LoginAPI

urlpatterns = [
    path('', views.get_users, name='Freelancers'),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
]
