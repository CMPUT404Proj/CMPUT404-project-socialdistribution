from django import forms
from .models import Post

#Adapted from http://tutorial.djangogirls.org/en/django_forms/index.html, March 6, 2016
class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('post_text', 'post_title', 'post_type', 'privacy',)