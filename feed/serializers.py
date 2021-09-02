from rest_framework import serializers

from feed.models import Post


class GetPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'price',
            'short_description',
            'payment',
            'reviews'
        ]


class GetPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'price',
            'description',
            'payment',
            'reviews',
            'vote'
        ]
