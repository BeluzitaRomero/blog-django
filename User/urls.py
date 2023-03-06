from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    #login
    path('login/', views.login_request, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(template_name='User/logout.html'),name='logout'),

    path('edit-profile/', views.edit_profile, name ='edit-profile'),
    path('edit-avatar/', views.create_avatar, name ='edit-avatar'),
]