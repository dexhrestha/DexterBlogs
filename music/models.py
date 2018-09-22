from django.db import models
from django.urls import reverse
from django.contrib.auth.models import Permission,User
# Create your models here.
class Album(models.Model):
	# id = models.Integer()
	user = models.ForeignKey(User,default=2,on_delete=models.CASCADE)
	artist = models.CharField(max_length=256)
	album_title = models.CharField(max_length=512)
	genre = models.CharField(max_length=64)
	album_logo = models.FileField()

	def get_absolute_url(self):
		return reverse('music:detail',kwargs={'pk':self.pk})

	def __str__(self):
		return self.album_title+' by '+self.artist
#needs to be associated with Album/specification of Album
class Song(models.Model):
	#total dependency if album is deleted song is deleted
	album = models.ForeignKey(Album,on_delete=models.CASCADE) 
	file_type = models.CharField(max_length = 8)
	song_title = models.CharField(max_length = 256)
	song_url = models.CharField(max_length=512,default="")
	is_favorite = models.BooleanField(default=False)

	def __str__(self):
		return self.song_title+' - '+self.file_type
