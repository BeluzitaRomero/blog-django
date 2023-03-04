from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_posts, name='all-posts'),
    path('post-detail/<pk>', views.post_detail, name='post-detail'),
    path('post-form', views.post_form, name='post-form'),
    path('delete-post/<pk>', views.delete_post, name='delete-post'),
    path('update-post/<pk>', views.update_post, name='update-post'),
]
