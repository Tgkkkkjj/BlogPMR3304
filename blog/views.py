from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm

# List View 
class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

# Detail View 
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

# Create View 
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_create.html'
    success_url = reverse_lazy('post_list')

# Update View 
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_create.html'
    success_url = reverse_lazy('post_list')

# Delete View
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('post_list')