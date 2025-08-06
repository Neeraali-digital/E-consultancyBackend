from rest_framework import generics, filters, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Course, College, Blog, Review
from .serializers import CourseSerializer, CollegeSerializer, BlogSerializer, ReviewSerializer

class CollegeListCreateView(generics.ListCreateAPIView):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'location']

class CollegeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer
    permission_classes = [AllowAny]

class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'code']

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]

class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [AllowAny]

class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [AllowAny]

@api_view(['GET'])
@permission_classes([AllowAny])
def college_stats(request):
    total = College.objects.count()
    active = College.objects.filter(status='active').count()
    by_type = {}
    for choice in College.TYPE_CHOICES:
        by_type[choice[0]] = College.objects.filter(type=choice[0]).count()
    
    return Response({
        'total': total,
        'active': active,
        'inactive': total - active,
        'byType': by_type
    })

@api_view(['GET'])
@permission_classes([AllowAny])
def course_stats(request):
    total = Course.objects.count()
    active = Course.objects.filter(status='active').count()
    by_category = {}
    for choice in Course.CATEGORY_CHOICES:
        by_category[choice[0]] = Course.objects.filter(category=choice[0]).count()
    
    return Response({
        'total': total,
        'active': active,
        'inactive': total - active,
        'byCategory': by_category
    })

@api_view(['POST'])
def toggle_course_status(request, pk):
    try:
        course = Course.objects.get(pk=pk)
        course.status = 'inactive' if course.status == 'active' else 'active'
        course.save()
        return Response(CourseSerializer(course).data)
    except Course.DoesNotExist:
        return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)
