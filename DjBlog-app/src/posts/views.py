from django.shortcuts import render 
from .models import Post , Comment 
from .forms import PostForm

# Create your views here.

def post_list(request):
    data = Post.objects.all()
    return render(request,'all_posts.html',{'posts':data})




def post_detail(request,post_id):
    data = Post.objects.get(id=post_id)
    return render(request , 'post.html' ,{'post':data})


def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
    else:
        form = PostForm()
    return render(request,'add_post.html',{'form':form})