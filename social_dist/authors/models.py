from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Author(models.Model):
	author_id = models.CharField(max_length=38, unique=True, default=uuid.uuid4)
	user = models.OneToOneField(User, primary_key=True)
	url = models.URLField(blank=True)
	host = models.CharField(max_length=100, default=settings.LOCAL_HOST)
	profile_pic = models.ImageField(upload_to='profile_images/', blank=True)

	def __unicode__(self): # unicode for Python 2.
		return self.user.username

	def get_absolute_image_url(self):
		return "{0}{1}".format('/profile_images/', self.profile_pic.url)

	def getFriends(self):
		# http://stackoverflow.com/questions/431628/how-to-combine-2-or-more-querysets-in-a-django-view 2016-03-06
		# current local author can be the first OR second.
		localFriends = LocalRelation.objects.filter(Q(author1=self) | Q(author2=self))


class GlobalAuthor(models.Model):
	global_author_id = models.CharField(max_length=38, unique=True, default=uuid.uuid4)
	global_author_name = models.CharField(max_length=50)
	url = models.URLField(blank=True)
	host = models.CharField(max_length=100, default=settings.LOCAL_HOST) # need to come up with a default host. it CANNOT be local host.

	def __unicode__(self): # unicode for Python 2.
		return self.global_author_name

class LocalRelation(models.Model):
	author1 = models.ForeignKey(Author, related_name="author1")
	author2 = models.ForeignKey(Author, related_name="author2")

	# False = not friends; True = mutual friends
	relation_status = models.BooleanField(default=False)

class GlobalRelation(models.Model):
	# https://docs.djangoproject.com/en/1.9/topics/db/models/ 2016-03-06
	STATUS_OPTIONS = (
		(0, 'FOLLOWS'), # local author follows remote (global) author
		(1, 'FOLLOWED'), # remote author follows local author
		(2, 'FRIENDS') # friends
	)

	local_author = models.ForeignKey(Author, related_name="local_author")
	global_author = models.ForeignKey(Author, related_name="global_author")

	relation_status = models.CharField(max_length=9, choices=STATUS_OPTIONS, default=0)

	# Tried to https://docs.djangoproject.com/en/1.8/topics/db/models/#intermediary-manytomany
	# but we are dealing with local and global authors, so there has to be 2 different relationships.