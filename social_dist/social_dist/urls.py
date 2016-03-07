from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'authors.views.user_login', name='login'),
    url(r'^register/', 'authors.views.register', name='register'),
    url(r'^logout/', 'authors.views.logout', name='logout'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^',include('stream.urls',namespace='stream')),
    url(r'^authors/',include('authors.urls',namespace='authors')),
    url(r'^friends/',include('friends.urls',namespace='friends')),
    url(r'^posts/',include('posts.urls',namespace='posts')),
    url(r'^author/posts/', 'posts.views.show_posts', name='show_posts'),
    url(r'^admin/', include(admin.site.urls)),
]
