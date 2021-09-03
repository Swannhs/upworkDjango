from django.contrib.auth.models import User

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from freelancer.serializers import FreelancerSerializer


@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = FreelancerSerializer(users, many=True)
    return Response(serializer.data, HTTP_200_OK)
