from django.http import Http404
# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render,get_object_or_404
from .models import Album,Song
# Create your views here.
def index(request):
	all_albums = Album.objects.all()
	#template looks for a templates folder
	# template = loader.get_template('music/index.html')
	context = {	'all_albums' : all_albums,}
	# return HttpResponse(template.render(context,request))
	return render(request,'music/index.html',context)

def detail(request,album_id):
	album=get_object_or_404(Album,pk=album_id)
	return render(request,'music/details.html',{'album':album})

def favorite(request,album_id):
	album=get_object_or_404(Album,pk=album_id)
	try:
		print(request.POST['song'])
		selected_song = album.song_set.get(pk=request.POST['song'])
	except (KeyError,Song.DoesNotExist):
		return render(request,'music/details.html',{'album':album,'err_msg':'Err 404 song not found'})
	else:
		selected_song.is_favorite= not selected_song.is_favorite
		selected_song.save()
		return render(request,'music/details.html',{'album':album})