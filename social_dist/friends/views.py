from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from authors.models import Author
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response

@login_required
def index(request):
	# this method also allows user to view local and global friends.
	author = Author.objects.get(user=request.user)

	context = dict()
	context['current_author'] = author
	context['local_friends'] = author.getLocalFriends()
	context['global_friends'] = author.getGlobalFriends()

	author.save()

	return render(request, 'friends/index.html', context)