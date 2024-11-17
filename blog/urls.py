from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/new/', views.post_form_view, name='create_post'),  # Creation
    path('post/<int:post_id>/edit/', views.post_form_view, name='edit_post'),  # Editing
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
]