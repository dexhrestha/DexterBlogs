
#url mappings for blog
from . import views
from django.conf.urls import include,url
app_name= 'blog'
urlpatterns = [
    url(r'^$',views.top_blogs,name='index'), #define the homepage for this
    url(r'^blogs/$',views.blogs,name='all_blogs'),
    url(r'^blog/(?P<blog_id>[0-9]+)/',views.blog,name='blog'),
]
