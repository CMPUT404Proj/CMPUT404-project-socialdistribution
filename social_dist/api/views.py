from django.http import HttpResponse
from django.shortcuts import render
from posts.models import Post
from posts.serializers import PostSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from rest_framework.response import Response

#http://www.django-rest-framework.org/tutorial/1-serialization/
#don't need this anymore
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@api_view(['GET','POST'])
def index(request):
	'''List all posts'''
	if request.method == 'GET':
		posts = Post.objects.all()
		serializer = PostSerializer(posts, many=True)
		return Response({"query": "posts", "count": len(posts), "size": 50, "next": "", "previous": "", "posts": serializer.data})
	elif request.method == 'POST':
		serializer = PostSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def queryFriends(request, uuid):
	return HttpResponse("hello")

def queryFriend2Friend(request, uuid1, uuid2):
	return HttpResponse("hello")

def getPosts(request):
	return HttpResponse("hello")

def getProfile(request, uuid):
	return HttpResponse("hello")

def authorPost(request, uuid):
	return HttpResponse("hello")

def singlePost(request, uuid):
	return HttpResponse("hello")

#http://www.django-rest-framework.org/tutorial/1-serialization/
#http://www.django-rest-framework.org/tutorial/2-requests-and-responses/
#TODO: size needs to be set, also paging
#TODO: needs to put comments in posts
#TODO: POST should insert post?
@api_view(['GET', 'POST'])
def publicPosts(request):
	'''List all public posts'''
	if request.method == 'GET':
		posts = Post.objects.all()
		serializer = PostSerializer(posts, many=True)
		return Response({"query": "posts", "count": len(posts), "size": 50, "next": "", "previous": "", "posts": serializer.data})
	elif request.method == 'POST':
		serializer = PostSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def comments(request, uuid):
	return HttpResponse("hello")

def friendRequest(request):
	return HttpResponse("hello")