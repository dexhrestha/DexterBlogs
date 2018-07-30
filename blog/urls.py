
#url mappings for blog
from . import views
from django.conf.urls import include,url
urlpatterns = [
    url(r'^$',views.blog,name='index'), #define the homepage for this
]
