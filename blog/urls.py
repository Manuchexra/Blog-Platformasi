from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('post/<int:pk>/comment/', views.add_comment, name='add_comment'),
    
    path('register/', views.register, name='register'),

    # Tizimga kirish
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),

    # Tizimdan chiqish
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
]