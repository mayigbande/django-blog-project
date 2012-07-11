# Create your views here.
"""
This code should be copied and pasted into your blog/views.py file before you begin working on it.
"""

from django.template import Context, loader
from django.http import HttpResponse

from models import Post, Comment 


def post_list(request):
    post_list = Post.objects.all()
    t=loader.get_template('blog/post_list.html')
    c=Context({'list':post_list})
    print type(post_list)
    print post_list
    
    return HttpResponse(t.render(c))
    #return HttpResponse(post_list)

def post_detail(request, id, showComments=False):
        post_detail=Post.objects.get(pk=id)
        t=loader.get_template('blog/post_detail.html')
        
        if showComments!=False:
		showComment=Comment.objects.filter(post=id)
		c=Context({'detail':post_detail,'comment':showComment})
		return HttpResponse(t.render(c))
	con=Context({detail:post_detail})
	return HttpResponse(t.render(con))
    #pass
    
def post_search(request, dede):
	term=Post.objects.filter(body__contains=dede)
	t=loader.get_template('blog/post_search.html')
	c=Context({'search_query':term})
	return HttpResponse(t.render(c))

   #pass

def home(request):
    print 'it works'
    return HttpResponse('hello world. Ete zene?') 
