from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'authors.views.login'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^',include('stream.urls',namespace='stream')),
    url(r'^authors/',include('authors.urls',namespace='authors')),
    url(r'^friends/',include('friends.urls',namespace='friends')),
    url(r'^posts/',include('posts.urls',namespace='posts')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/', include('authors.login_urls')),
    url(r'^logout/', 'authors.views.logout', name='logout'),
]
