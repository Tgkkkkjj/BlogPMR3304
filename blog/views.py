from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.shortcuts import get_object_or_404, redirect
from .models import Post, Comment


# List View 
class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

# Detail View  - Sem Uso de Forms
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()  # Exibe todos os comentários associados ao post
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        body = request.POST.get('body')  # Captura o texto do comentário enviado no campo 'body'
        if body:  # Se o corpo do comentário não estiver vazio
            comment = Comment(post=self.object, body=body)
            if request.user.is_authenticated:
                comment.author = request.user  # Se o usuário estiver autenticado, associa o comentário a ele
            comment.save()
        return redirect('post_detail', pk=self.object.pk)  # Redireciona para a página do post
    
    

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

# Delete Viewa
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    context_object_name = 'post'
    success_url = reverse_lazy('post_list')