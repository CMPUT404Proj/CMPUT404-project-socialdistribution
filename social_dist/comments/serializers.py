from rest_framework import serializers
from posts.models import Post
from authors.serializers import AuthorSerializer

class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    id = serializers.SerializerMethodField('get_post_id')

    def get_post_id(self, obj):
        return obj.post_id

    class Meta:
        model = Post
        fields = ('title', 'source', 'origin', 'description', 'contentType', 'content', 'author', 'published', 'id', 'visibility')
