from django.contrib import admin
from blog.models import Post, Category

# Configuração do modelo Category no admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  
    search_fields = ('name',)  

# Configuração do modelo Post no admin
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on', 'last_modified') 
    search_fields = ('title', 'body')  
    list_filter = ('created_on', 'categories') 
    filter_horizontal = ('categories',)  