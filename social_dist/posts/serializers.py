from rest_framework import serializers
from posts.models import Post
from authors.serializers import AuthorSerializer

class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ('author','post_id','pub_date','post_text','post_title','post_type','privacy')