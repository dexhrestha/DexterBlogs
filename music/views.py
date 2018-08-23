from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import Album,Song
from django.urls import reverse_lazy
from .forms import UserForm,LoginForm
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

class DetailView(generic.DetailView):
	model = Album
	template_name = 'music/details.html'
		
class AlbumCreate(CreateView):
	model = Album
	fields=['artist','album_title','genre','album_logo']

class AlbumUpdate(UpdateView):
	model = Album
	fields=['artist','album_title','genre','album_logo']

class AlbumDelete(DeleteView):
	model = Album
	success_url = reverse_lazy('music:index')

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


