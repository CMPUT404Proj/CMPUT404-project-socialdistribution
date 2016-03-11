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
	github = models.URLField(blank=True)

	def __unicode__(self): # unicode for Python 2.
		return self.user.username

	def get_absolute_image_url(self):
		return "{0}{1}".format('/profile_images/', self.profile_pic.url)

	def getLocalFriends(self):
		# http://stackoverflow.com/questions/431628/how-to-combine-2-or-more-querysets-in-a-django-view 2016-03-06
		# current local author can be the first OR second.
		localRelations = LocalRelation.objects.filter((models.Q(author1=self) | models.Q(author2=self)) & models.Q(relation_status=True))
		
		localFriends = []

		for relation in localRelations:
			if relation.author1 == self:
				# add author's friend
				localFriends.append(relation.author2)
			elif relation.author2 == self:
				# add author's friend
				localFriends.append(relation.author1)

		return localFriends

	def getGlobalFriends(self):

		globalRelations = GlobalRelation.objects.filter(models.Q(local_author=self) & models.Q(relation_status=2))

		globalFriends = []

		for relation in globalRelations:
			if relation.local_author == self:
				# add global friend
				globalFriends.append(relation.global_author)

		return globalFriends

	# Get all friend requests sent by current user (includes local and global)
	def getAllPendingFriendRequestsSent(self):
		
		# per requirements: 
		# When adding friend, automatically follow the user added. Therefore relation status should be False.
		PendingLocalRelations = LocalRelation.objects.filter(author1=self, relation_status=False)

		PendingGlobalRelations = GlobalRelation.objects.filter(local_author=self, relation_status=0)

		sent_requests = []

		for relation in PendingLocalRelations:
			sent_requests.append(relation.author2)

		for relation in PendingGlobalRelations:
			sent_requests.append(relation.global_author)

		return sent_requests

	# Get all friend requests recieve by current user (includes local and global)
	def getAllPendingFriendRequestsRecieved(self):
		# author2 added/follows author1 (the current user)
		PendingLocalRelations = LocalRelation.objects.filter(author2=self, relation_status=False)

		PendingGlobalRelations = GlobalRelation.objects.filter(local_author=self, relation_status=1)

		recieved_requests = []

		for relation in PendingLocalRelations:
			recieved_requests.append(relation.author1)

		for relation in PendingGlobalRelations:
			recieved_requests.append(relation.global_author)

		return recieved_requests

	def getFriendNames(self):
		local_friends = self.getLocalFriends()
		global_friends = self.getGlobalFriends()

		local_usernames = []
		for friend in local_friends:
			local_usernames.append(friend.user.username)

		global_usernames = []
		for friend in global_friends:
			global_usernames.append(friend.global_author_name)

		return local_usernames, global_usernames

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

	# False = author1 follows author2; True = author1 follows AND IS friends with author2
	relation_status = models.BooleanField(default=False)

class GlobalRelation(models.Model):
	# https://docs.djangoproject.com/en/1.9/topics/db/models/ 2016-03-06
	STATUS_OPTIONS = (
		(0, 'FOLLOWS'), # local author follows remote (global) author
		(1, 'FOLLOWED'), # remote author follows local author
		(2, 'FRIENDS') # friends
	)

	local_author = models.ForeignKey(Author, related_name="local_author")
	global_author = models.ForeignKey(GlobalAuthor, related_name="global_author")

	relation_status = models.CharField(max_length=9, choices=STATUS_OPTIONS, default=0)

	# Tried to https://docs.djangoproject.com/en/1.8/topics/db/models/#intermediary-manytomany
	# but we are dealing with local and global authors, so there has to be 2 different relationships.