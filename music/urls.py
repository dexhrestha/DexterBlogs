from django.conf.urls import url
from . import views
app_name= 'music'
urlpatterns=[
	#/music/
	# url(r'^$',views.index,name ='index'),
	url(r'^$',views.index,name='index'), # using generic/class
	url(r'^login/$',views.LoginView.as_view(),name='login'),
	url(r'^logout/$',views.logout_user,name='logout'),
	url(r'^register/$',views.UserFormView.as_view(),name='register'),
	#/music/21/
	#()-group as 21 not as 2 and 1 seperated, ?P<album_id>=>store 21 into album_id var
	#url(r'^(?P<album_id>[0-9]+)/$',views.detail,name='detail') ,	using function in views
	url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'), #using generic/class , it expects pk so use pk
	#/music/<album_id>/favorite
	#url(r'^(?P<album_id>[0-9]+)/favorite/$',views.favorite,name='favorite'), 	
	#/music/album/add/
	url(r'^album/add/$',views.AlbumCreate.as_view(),name='album_add'),
	#/music/album/2/
	url(r'^album/(?P<pk>[0-9]+)/$',views.AlbumUpdate.as_view(),name='album_edit'),
	#/music/album/2/delete/
	url(r'^album/(?P<pk>[0-9]+)/delete/$',views.AlbumDelete.as_view(),name='album_delete'),

]