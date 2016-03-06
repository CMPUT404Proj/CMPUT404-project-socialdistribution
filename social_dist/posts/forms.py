from django import forms
from .models import Post

#Adapted from http://tutorial.djangogirls.org/en/django_forms/index.html, March 6, 2016
class PostForm(forms.ModelForm):
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
	post_text = forms.TextField(label='Content')
	post_title = forms.CharField(label='Title', max_length=64)
	post_type = forms.CharField(label='Type', max_length=2, choices=POST_TYPE_CHOICES,default='PT')
	privacy = forms.CharField(label='Privacy',max_length=4, choices=PRIVACY_CHOICES,default='PB')