from django.shortcuts import render
def index(request):
	return HttpResponse("Hello you're at posts index")
