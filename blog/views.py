from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
from .models import Post

# Create/Edit Post View
def post_form_view(request, post_id=None):
    post = None
    if post_id:  # If post_id is provided, we're editing
        post = get_object_or_404(Post, id=post_id)
        form = PostForm(request.POST or None, instance=post)
    else:  # If no post_id, we're creating a new post
        form = PostForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('post_list')

    return render(request, 'post_create.html', {'form': form, 'post': post})

# Read (list all posts)
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

# Read (individual post)
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post': post})

# Delete
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        post.delete()
        return redirect('post_list')
    return render(request, 'post_confirm_delete.html', {'post': post})