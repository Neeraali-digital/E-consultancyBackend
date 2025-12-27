from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserListCreateView.as_view(), name='user-list-create'),
    path('users/admin/', views.create_admin_view, name='create-admin'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('roles/', views.RoleListCreateView.as_view(), name='role-list-create'),
    path('auth/login/', views.login_view, name='login'),
    path('auth/register/', views.register_view, name='register'),
    path('auth/logout/', views.logout_view, name='logout'),
]