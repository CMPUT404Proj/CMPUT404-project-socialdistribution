from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm
from .models import Author
from django.contrib.auth import get_user_model
from django.utils import timezone

def index(request):
	return HttpResponse("Hello you're at posts index")

#adapted from http://tutorial.djangogirls.org/en/django_forms/index.html
def post_new(request):
	if request.method == "POST":
		form = PostForm(data=request.POST)
		print(form.errors)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = Author.objects.get(user=request.user)
			post.pub_date = timezone.now()
			post.save()
	else:
		form = PostForm()
	return render(request, 'authors/index.html', {'form':form})
