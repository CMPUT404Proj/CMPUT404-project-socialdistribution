from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from authors.models import Author, GlobalAuthor
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

	return render(request, 'friends/index.html', context)

@login_required
def search(request):
	# TODO: not finished with this yet.
	if request.method == 'POST':
		search_id = request.POST.get('search_field', None)
		try:
			# Get all local users.
			users = User.objects.filter(username__icontains=search_id)
			local_names = []
			for user in users:
				local_names.append(user.username)

			# Get all Remote users.
			global_users = GlobalAuthor.objects.filter(global_author_name__icontains=search_id)
			global_names = []
			for user in global_users:
				global_names.append(user.global_author_name)

			# Return all usernames
			usernames = dict()
			usernames["local_names"] = local_names
			usernames["global_names"] = global_names

			return HttpResponse(usernames)
		except User.DoesNotExist:
			return HttpResponse("No such user found.")
	else:
		return render(request, 'friends/index.html')
