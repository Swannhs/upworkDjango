from knox.auth import TokenAuthentication
from rest_framework import permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_201_CREATED, \
    HTTP_400_BAD_REQUEST

from feed.models import Post
from feed.serializers import GetPostsSerializer, GetPostSerializer, MakePostSerializer


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_posts(request):
    try:
        posts = Post.objects.all()
        serializer = GetPostsSerializer(posts, many=True)
        return Response({
            'data': serializer.data,
            'results': len(serializer.data)
        }, HTTP_200_OK)
    except:
        return Response({
            'message': 'Error to retrieve posts'
        }, HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_post(request, id):
    try:
        post = Post.objects.get(id=id)
        serializer = GetPostSerializer(post, many=False)
        return Response({
            'data': serializer.data,
        }, HTTP_200_OK)
    except:
        return Response({
            'message': 'Post not exist'
        }, HTTP_404_NOT_FOUND)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def make_post(request):
    serializer = MakePostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=HTTP_201_CREATED)
    else:
        return Response(status=HTTP_400_BAD_REQUEST)
