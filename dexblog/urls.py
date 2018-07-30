
#url mappings
from django.contrib import admin
from django.conf.urls import include,url

urlpatterns = [
	url(r'^', include('blog.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^music/', include('music.urls')),
    url(r'^blog/', include('blog.urls')),
]
