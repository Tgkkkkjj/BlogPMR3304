from django import forms
from .models import Post, Category

class PostForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,  # Categorias são opcionais
        label="Categorias"
    )

    class Meta:
        model = Post
        fields = ['title', 'body', 'categories']