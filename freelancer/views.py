from django.contrib.auth import login
from django.contrib.auth.models import User

# Create your views here.
from rest_framework import generics, permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from knox.views import LoginView as KnoxLoginView
from freelancer.serializers import FreelancerSerializer


@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = FreelancerSerializer(users, many=True)
    return Response(serializer.data, HTTP_200_OK)


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = FreelancerSerializer
    permission_classes = (AllowAny,)


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
