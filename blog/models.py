from django.contrib import admin
from django.db import models
class Post(models.Model):
	title=models.CharField(max_length=255)
	body=models.TextField()
	date_created=models.DateField()
	date_updated=models.DateField()
class Comment(models.Model):
	body =models.TextField()
	author=models.CharField(max_length=60)
	date_created=models.DateField()
	date_updated=models.DateField()
	post=models.ForeignKey(Post)

admin.site.register(Post)
admin.site.register(Comment)
	
# Create you models here.
