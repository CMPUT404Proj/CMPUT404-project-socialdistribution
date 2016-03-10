from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import PostForm
from .models import Author
from .models import Post
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
@login_required
def index(request):
	return HttpResponse("Hello you're at posts index")

#adapted from http://tutorial.djangogirls.org/en/django_forms/index.html
@login_required
def post_new(request):
	if request.method == "POST":
		form = PostForm(data=request.POST)
		print(form.errors)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = Author.objects.get(user=request.user.id)
			post.published = timezone.now()
			post.save()
			#return redirect('show_posts')
			return HttpResponseRedirect('/profile')
			#return render(request, 'authors/index.html', {'form':form})
	else:
		form = PostForm()
	return render(request, 'authors/index.html', {'form':form})
@login_required
def show_posts(request):
	print "gets to this point"
	posts = Post.objects.filter(published__lte=timezone.now()).order_by('-published')
	print posts
	return render(request,'authors/index.html', {'posts':posts})

@login_required
def delete_post(request):
	if request.method == "POST":
		print("id: %s"%request.POST.get("post_id"))
		post = Post.objects.get(post_id=request.POST.get("post_id"))
		print post
		if post != None:
			post.delete()
			return HttpResponseRedirect('/profile')
		else:
			#TODO: this should return 404
			return HttpResponseRedirect('/profile')
		

