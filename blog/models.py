from django.contrib import admin
from django.db import models
class Post(models.Model):
	title=models.CharField(max_length=255)
	body=models.TextField()
	date_created=models.DateField(auto_now_add=True)
	date_updated=models.DateField(auto_now=True)
	def __unicode__(self):
		return self.title
class Comment(models.Model):
	body =models.TextField()
	author=models.CharField(max_length=60)
	date_created=models.DateField(auto_now_add=True)
	date_updated=models.DateField(auto_now=True)
	post=models.ForeignKey(Post)
	def first_60(self):
		return self.body[:60]
	def __unicode__(self):
		return self.body
class CommentInLine(admin.TabularInline):
	model=Comment
class PostAdmin(admin.ModelAdmin):
	list_display=('title','date_created','date_updated')
	search_fields=('title','body')
	list_filter=('date_created',)
	inlines=[CommentInLine]
class CommentAdmin(admin.ModelAdmin):
	list_display=('post','author','first_60','date_created','date_updated')
	list_filter=('date_created','author')


admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
	
# Create you models here.
