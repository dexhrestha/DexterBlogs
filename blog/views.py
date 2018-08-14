from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Blog
# Create your views here.
def blogs(request):
	all_blogs = Blog.objects.all()
	content = {'all_blogs':all_blogs}
	return render(request,'blog/blogs.html',content)

def blog(request,blog_id):
	blog = get_object_or_404(Blog,pk=blog_id)
	content = {'blog':blog}
	return render(request,'blog/blog.html',content)

def top_blogs(request):
	top = []
	for x in [1,2]:
		blog = get_object_or_404(Blog,pk=x)
		top.append(blog)
	content = {'top':top}
	return render(request,'blog/index.html',content)
