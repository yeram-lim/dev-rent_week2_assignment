from django.shortcuts import render, redirect, get_object_or_404
from django.urls import include
from .models import Post
from .forms import PostForm


# Create your views here.


def base(request):
    posts = Post.objects.all()
    ctx = {'posts': posts}
    return render(request, "post/base.html", ctx)

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    ctx = {'post': post}
    return render(request, "post/detail.html", ctx)

def post_write(request):
    if request.method == "POST":
        write_form = PostForm(request.POST)
        if write_form.is_valid():
            write_form.save()
            return redirect("post:base")
    else:
        write_form = PostForm()
        ctx = {'write_form' : write_form}

    return render(request, "post/write.html", ctx)

def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post:detail', pk) #수정 끝나고 저장하면 확인 위해 상세페이지로 이동한다.
    else:
        form = PostForm(instance=post)
        ctx = {'form' : form}

    return render(request, "post/update.html", ctx)

def post_delete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('post:base')

