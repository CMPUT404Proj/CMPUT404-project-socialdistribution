from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'social_dist.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^',include('authors.urls',namespace='authors')),
    url(r'^authors/',include('authors.urls',namespace='authors')),
    url(r'^posts/',include('posts.urls',namespace='posts')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/', include('authors.urls',namespace='authors')),
]
