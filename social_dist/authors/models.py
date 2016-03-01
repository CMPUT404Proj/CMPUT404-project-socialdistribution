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
