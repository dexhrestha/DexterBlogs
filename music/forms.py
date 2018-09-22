from django.contrib.auth.models import User
from .models import Song,Album
from django import forms

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ['username','email','password']

class SongForm(forms.ModelForm):
	class Meta:
		model = Song
		fields = ['song_title','file_type','is_favorite','song_url']

class AlbumForm(forms.ModelForm):
	class Meta:
		model = Album
		fields = ['artist','album_title','genre','album_logo']

class LoginForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ['username','password']

		
		