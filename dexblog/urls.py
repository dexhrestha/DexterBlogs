
#url mappings
from django.contrib import admin
from django.conf.urls import include,url
from django.conf import settings 
from django.conf.urls.static import static
urlpatterns = [
	url(r'^', include('blog.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^music/', include('music.urls')),
    url(r'^myblog/', include('blog.urls')),
]

if settings.DEBUG:
	print(settings.STATIC_URL, settings.STATIC_ROOT)
	urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
