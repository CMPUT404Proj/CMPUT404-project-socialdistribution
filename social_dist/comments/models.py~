from django.db import models
from django.conf import settings
from authors.models import Author
from posts.models import Post
import uuid

class Comment(models.Model):
	
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post =models.ForeignKey(Post, on_delete=models.CASCADE)
	comment_id = models.CharField(max_length=38, unique=True, default=uuid.uuid4)
	pub_date = models.DateTimeField('date published')
	comment_text = models.TextField()
	
	def __str__(self):
		return self.comment_text
