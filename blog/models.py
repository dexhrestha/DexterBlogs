from django.db import models
from datetime import datetime
# Create your models here.
class Blog(models.Model):
	blog_title = models.CharField(max_length=512)
	author = models.CharField(max_length=256)
	date = models.DateTimeField(default=datetime.now())
	media = models.CharField(max_length=256)
	article = models.TextField()
	category = models.CharField(max_length=32)

	def __str__(self):
		return self.blog_title+' by '+self.author