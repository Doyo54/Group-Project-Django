from django.shortcuts import render, redirect,HttpResponseRedirect,get_object_or_404
from .models import Comment,Post
from .forms import PostForm,CommentForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = PostForm()
    loops = {
        'posts': posts,
        'form': form,
    }
    return render(request, 'index.html',loops)

def post_comment(request, id):
    posts = get_object_or_404(Post, pk=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            savecomment = form.save(commit=False)
            savecomment.post = posts
            savecomment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = CommentForm()
    return render(request, 'comment.html', { 'posts': posts,'form': form,})