from rest_framework import serializers
from authors.models import Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('author_id','user','url','host','profile_pic')