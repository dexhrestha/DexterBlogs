from django.views import generic
from django.http import JsonResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate,login,logout
from .models import Album,Song
from django.urls import reverse_lazy
from .forms import UserForm,LoginForm,SongForm
from django.views.generic.base import View

#Using generic/class
'''class IndexView(generic.ListView):
	template_name = 'music/index.html'
	context_object_name = 'all_albums' #default value is 'object_list'

	def get_queryset(self,request):
		if not request.user.is_authenticated():
			return render(request,'music/login.html')
		else:
			albums = Album.objects.filter(user=request.user)'''
def index(request):
	if not request.user.is_authenticated:
		return redirect('music:login')
	else:
		albums = Album.objects.filter(user=request.user)
		return render(request,'music/index.html',{'all_albums':albums})

def detail(request,pk):
	if not request.user.is_authenticated:
		return render(request,'music/login.html')
	else:
		user = request.user
		album = get_object_or_404(Album,pk=pk)
		return render(request,'music/details.html',{'album':album,'user':user})

class AlbumCreate(CreateView):
	model = Album
	fields=['artist','album_title','genre','album_logo']

class AlbumUpdate(UpdateView):
	model = Album
	fields=['artist','album_title','genre','album_logo']

class AlbumDelete(DeleteView):
	model = Album
	success_url = reverse_lazy('music:index')

class SongCreate(CreateView):
	model = Song
	fields = ['album','file_type','song_title','is_favorite']

class UserFormView(View):
	form_class = UserForm
	template_name = 'music/registration_form.html'

	#display blank form
	def get(self,request):
		form = self.form_class(None)
		return render(request,self.template_name,{'form':form})
	#process form data
	def post(self,request):
		form = self.form_class(request.POST) #contains all contents of form

		if form.is_valid():
			#create an object from form but doesnot save at database yet
			user = form.save(commit=False)

			#clean (normalized) data => properly formatted
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			#returns Use objects if credentials correct
			user = authenticate(username=username,password=password)

			if user is not None:
				#check if user is active
				if user.is_active:
					login(request,user)
					return redirect('music:index')
		return render(request,self.template_name,{'form':form})

class LoginView(View):
	form_class = LoginForm
	template_name = 'music/login.html'

	def get(self,request):
		form = self.form_class(None)
		return render(request,self.template_name,{'form':form})

	def post(self,request):
		print('Post login')
		form = self.form_class(request.POST)
			
		print('Form valid')
		username = request.POST['username']
		password = request.POST['password']
	#authenticate user credentials
		user = authenticate(username=username,password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				albums = Album.objects.filter(user=request.user)
				return render(request,'music/index.html',{'all_albums':albums,'user':request.user.username})
			else:
				return render(request,self.template_name,{'err_msg':'Your account has been disabled. Contact the administrator.','form':form})
		else:
			return render(request,self.template_name,{'err_msg':'Invalid Login.','form':form})
		return render(request,self.template_name,{'form':form})


def logout_user(request):
	logout(request)
	return redirect('music:index')

def create_song(request,pk):
	form =  SongForm(request.POST or None,)
	album = get_object_or_404(Album,pk=pk)
	if form.is_valid():
		albums_songs = album.song_set.all()
		for s in albums_songs:
			if s.song_title == form.cleaned_data.get("song_title"):
				context={
					'album':album,
					'form':form,
					'error_message': 'You already added that song',
				}
				return render(request,'music/song_form.html',context)
		song = form.save(commit=False)
		song.album = album
		song.save()

	return render(request,'music/song_form.html',{'album':album,'form':form})

def delete_song(request,pk,song_id):
	album = get_object_or_404(Album,pk=pk)
	song = Song.objects.get(pk=song_id)
	song.delete()
	return render(request,'music/details.html',{'album':album})

def favorite_song(request,song_id):
	song = get_object_or_404(Song,pk=song_id)
	try:
		if song.is_favorite:
			song.is_favorite = False
		else:
			song.is_favorite = True
		song.save()
	except (KeyError,Song.DoesNotExist):
		return JsonResponse({'success':False})
	else:
		return JsonResponse({'success':True})
