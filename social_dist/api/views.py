from django.http import HttpResponse
from django.shortcuts import render
from posts.models import Post
from posts.serializers import PostSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import JsonResponse

#http://www.django-rest-framework.org/tutorial/1-serialization/
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def index(request):
	'''List all posts'''
	if request.method == 'GET':
		posts = Post.objects.all()
		serializer = PostSerializer(posts, many=True)
		return JSONResponse({"query": "posts", "count": len(posts), "size": 50, "next": "", "previous": "", "posts": serializer.data})
	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = PostSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data, status=201)
		return JSONResponse(serializer.erros, status=400)



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

def post(request, uuid):
	return HttpResponse("hello")

#http://www.django-rest-framework.org/tutorial/1-serialization/
#TODO: size needs to be set, also paging
#TODO: POST should insert post?
def publicPosts(request):
	'''List all public posts'''
	if request.method == 'GET':
		posts = Post.objects.all()
		serializer = PostSerializer(posts, many=True)
		return JSONResponse({"query": "posts", "count": len(posts), "size": 50, "next": "", "previous": "", "posts": serializer.data})
	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = PostSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data, status=201)
		return JSONResponse(serializer.erros, status=400)

def comments(request, uuid):
	return HttpResponse("hello")

def friendRequest(request):
	return HttpResponse("hello")