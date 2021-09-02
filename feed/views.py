from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from feed.models import Post
from feed.serializers import GetPostsSerializer


@api_view(['GET'])
def get_posts(request):
    posts = Post.objects.all()
    serializer = GetPostsSerializer(posts, many=True)
    return Response(serializer.data, HTTP_200_OK)