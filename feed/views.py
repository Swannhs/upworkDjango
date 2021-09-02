from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR

from feed.models import Post
from feed.serializers import GetPostsSerializer, GetPostSerializer


@api_view(['GET'])
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
