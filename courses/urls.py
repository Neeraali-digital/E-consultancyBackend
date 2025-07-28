from django.urls import path
from . import views

urlpatterns = [
    path('colleges/', views.CollegeListCreateView.as_view(), name='college-list-create'),
    path('colleges/<int:pk>/', views.CollegeDetailView.as_view(), name='college-detail'),
    path('colleges/stats/', views.college_stats, name='college-stats'),
    
    path('courses/', views.CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', views.CourseDetailView.as_view(), name='course-detail'),
    path('courses/<int:pk>/toggle-status/', views.toggle_course_status, name='course-toggle-status'),
    path('courses/stats/', views.course_stats, name='course-stats'),
    
    path('blogs/', views.BlogListCreateView.as_view(), name='blog-list-create'),
    path('blogs/<int:pk>/', views.BlogDetailView.as_view(), name='blog-detail'),
    
    path('reviews/', views.ReviewListCreateView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', views.ReviewDetailView.as_view(), name='review-detail'),
]