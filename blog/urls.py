from django.urls import path
from blog.views import BlogListAPIView, BlogDetailAPIView, CommentListAPIView

app_name='blog'

urlpatterns =[
    path("", BlogListAPIView.as_view(), name="blog_list"),
    path("<int:pk>/", BlogDetailAPIView.as_view(), name="blog_detail"),
    path('<int:pk>/comments/', CommentListAPIView.as_view(), name='comment_list')
]