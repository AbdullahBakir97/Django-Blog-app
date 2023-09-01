from django.shortcuts import render 
from .models import Post , Comment 

# Create your views here.

def post_list(request):
    data = Post.objects.all()
    return render(request,'all_post.html',{'posts':data})