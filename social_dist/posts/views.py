from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello you're at posts index")

#adapted from http://tutorial.djangogirls.org/en/django_forms/index.html
def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.pub_date = timezone.now()
			post.save()
	else:
		form = PostForm()
	return render(request, 'authors/index.html', {'form':form})
