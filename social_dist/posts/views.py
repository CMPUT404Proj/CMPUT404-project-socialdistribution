from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import PostForm
from .models import Author
from .models import Post
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

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
			post.published = timezone.now()
			post.save()
			#return redirect('authors:home')
			#return HttpResponseRedirect(reverse('authors:home'))
			return render(request, 'authors/index.html', {'form':form})
	else:
		form = PostForm()
	return render(request, 'authors/index.html', {'form':form})

def show_posts(request):
	print "gets to this point"
	posts = Post.objects.filter(published__lte=timezone.now()).order_by('-published')
	#posts = Post.objects
	print posts
	return render(request,'authors/index.html', {'posts':posts})
		

