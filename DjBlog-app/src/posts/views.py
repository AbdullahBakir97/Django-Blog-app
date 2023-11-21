from django.shortcuts import render , redirect
from .models import Post , Comment 
from .forms import PostForm

# Create your views here.

def post_list(request):
    data = Post.objects.all() # List        1 : query
    return render(request,'all_posts.html',{'posts':data}) # 3 things [requset, 'html', context{}]
                            # 2 : html page  3: context 

def post_detail(request,post_id):
    data = Post.objects.get(id=post_id)
    return render(request , 'post_detail' ,{'post':data})


def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
            return redirect('/blog/')
        
    else:
        form = PostForm()
    return render(request,'add_post.html',{'form':form})


def edit_post(request,post_id):
    data = Post.objects.get(id=post_id)
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES, instance=data)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
            return redirect('/blog/')
        
    else:
        form = PostForm(instance=data)
    return render(request,'edit_post.html',{'form':form})



def delete_post(request,post_id):
    data = Post.objects.get(id=post_id)
    data.delete()
    return redirect('/blog/')