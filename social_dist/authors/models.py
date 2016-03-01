from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Author(models.Model):
	author_id = models.CharField(max_length=38, unique=True, default=uuid.uuid4)
	user = models.OneToOneField(User, primary_key=True)
	url = models.URLField(blank=True)

	def __str__(self):
		return self.first_name + " " + self.last_name

class GlobalAuthor(models.Model):
	global_author_id = models.CharField(max_length=38, unique=True, default=uuid.uuid4)
	global_author_name = models.CharField(max_length=50)
	url = models.URLField(blank=True)

	def __str__(self):
		return self.global_author_name

class LocalRelation(models.Model):
	author1 = models.ForeignKey(Author, related_name="author1")
	author2 = models.ForeignKey(Author, related_name="author2")

	# False = not friends; True = mutual friends
	relation_status = models.BooleanField(default=False)

class GlobalRelation(models.Model):
	FOLLOWS = 0 # local author follows remote author
	FOLLOWED = 1 # remote author follows local author
	FRIENDS = 2 # mutual friends

	local_author = models.ForeignKey(Author, related_name="local_author")
	global_author = models.ForeignKey(Author, related_name="global_author")

	relation_status = models.PositiveIntegerField(default=FOLLOWS)