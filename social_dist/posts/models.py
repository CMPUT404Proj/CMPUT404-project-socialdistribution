from django.db import models
from django.conf import settings
from authors.models import Author
import uuid

class Post(models.Model):
	POST_TYPE_CHOICES = (
		('MD', 'Markdown'),
		('PT', 'Plain text'),
	)
	PRIVACY_CHOICES = (
		('PV', 'Private to me'),
		('PA', 'Private to another author'),
		('PF', 'Private to my friends'),
		('FOAF', 'Friend of a friend'),
		('HF', 'Private to only friends on my host'),
		('PB', 'Public'),
	)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	post_id = models.CharField(max_length=38, unique=True, default=uuid.uuid4)
	pub_date = models.DateTimeField('date published')
	post_text = models.TextField()
	post_title = models.CharField(max_length=64)
	post_type = models.CharField(max_length=2, choices=POST_TYPE_CHOICES,default='PT')
	privacy = models.CharField(max_length=4, choices=PRIVACY_CHOICES,default='PB')

	def __str__(self):
		return self.post_text