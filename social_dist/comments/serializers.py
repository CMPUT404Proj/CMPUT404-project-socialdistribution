from rest_framework import serializers
from posts.models import Post
from comments.models import Comment
from authors.serializers import AuthorSerializer

class CommentSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    id = serializers.SerializerMethodField('get_comment_id')

    def get_comment_id(self, obj):
        return obj.comment_id

    class Meta:
        model = Comment
        fields = ('author','comment_text','contentType','id','pub_date')
