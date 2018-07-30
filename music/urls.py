from django.conf.urls import url
from . import views
app_name= 'music'
urlpatterns=[
	#/music/
	url(r'^$',views.index,name ='index'),
	#/music/21/
	#()-group as 21 not as 2 and 1 seperated, ?P<album_id>=>store 21 into album_id var
	url(r'^(?P<album_id>[0-9]+)/$',views.detail,name='detail') ,	
	#/music/<album_id>/favorite
	url(r'^(?P<album_id>[0-9]+)/favorite/$',views.favorite,name='favorite'), 	
]