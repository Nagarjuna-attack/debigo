from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
	posts = Post.objects.all().order_by('-id')
	return render(request,'index.html',{'posts':posts})


def post(request, pk ):
	read = Post.objects.get(id=pk)
	return render(request,'post.html',{'read':read})