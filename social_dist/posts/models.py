from django.db import models
from django.conf import settings
import uuid

class Post(models.Model):
	POST_TYPE_CHOICES = (
		('MD', 'Markdown'),
		('PT', 'Plain text'),
	)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	post_id = models.CharField(max_length=38, unique=True, default=uuid.uuid4)
	pub_date = models.DateTimeField('date published')
	post_text = models.TextField()
	post_title = models.CharField(max_length=64)
	post_type = models.CharField(max_length=2, choices=POST_TYPE_CHOICES,default='PT')
	private = models.BooleanField(initial=true)

	def __str__(self):
		return self.post_text