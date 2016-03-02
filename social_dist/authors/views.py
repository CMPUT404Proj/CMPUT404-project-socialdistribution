from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from authors.forms import UserForm, AuthorProfileForm
from django.template import RequestContext
from django.shortcuts import render_to_response

#main source: http://www.tangowithdjango.com/book/chapters/login.html

@login_required
def index(request):
	return render(request, 'authors/index.html')

	# https://docs.djangoproject.com/es/1.9/topics/auth/default/
	#username = request.POST['username']
	#password = request.POST['password']
	#user = authenticate(username=username, password=password)

	#if user is not None:
	#	if user.is_active:
	#		login(request, user)
			# redirect to the author's page....
	#		return render(request, 'authors/index.html')

	# might just create a separate login method....

def register(request):
	context = RequestContext(request)
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = AuthorProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save();

			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False) # False because need to set user attributes ourselves.
			profile.user = user

			if 'profile_pic' in request.FILES:
				profile.profile_pic = request.FILES['profile_pic']

			profile.save()

			registered = True
		else:
			print user_form.errors, profile_form.errors
	else:
		user_form = UserForm()
		profile_form = AuthorProfileForm()

	# TODO: Need to find a way for settings to find this template, otherwise it's throwing:
	# 'TemplateDoesNotExist at /register/' 
	return render_to_response(
		'templates/register.html',
		{'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
		context)