# Create your views here.
"""
This code should be copied and pasted into your blog/views.py file before you begin working on it.
"""

from django.template import Context, loader
from django.http import HttpResponse

from models import Post, Comment 


def post_list(request):
    post_list = Post.objects.all()
    
    print type(post_list)
    print post_list
    
    return HttpResponse(post_list)
    #return HttpResponse(post_list)

def post_detail(request, id, showComments=False):
        post_detail=Post.objects.get(pk=id)
        if showComments!=False:
		showComment=Comment.objects.filter(post=id)
	return HttpResponse(showComment)
	return HttpResponse(post_detail)
    #pass
    
def post_search(request, dede):
	searching=Post.objects.filter(body__contains=dede)
	return HttpResponse(searching)

   #pass

def home(request):
    print 'it works'
    return HttpResponse('hello world. Ete zene?') 
