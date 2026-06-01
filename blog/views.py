from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.serializers import BlogListSerializer, BlogDetailSerializer, BlogDetailCommentSerializer, CommentSerializer
from blog.models import Blog, Comment

class BlogListAPIView(APIView):
    # 1) 전체 게시글 목록 불러오기 : GET /blogs/
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogListSerializer(blogs, many=True)
        return Response({
            "status": "HTTP 200 OK",
            "data": serializer.data, 
            })

    # 2) 게시글 작성하기 : POST /blogs/
    def post(self, request):
        serializer = BlogDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "HTTP 201 CREATED",
                "data": serializer.data
                })
        else:
            return Response({
                "status": "HTTP 400 BAD REQUEST",
                "error": serializer.errors
                })

class BlogDetailAPIView(APIView):
    # 3) 게시글 상세페이지 불러오기 : GET /blogs/{blog_id}
    def get(self, request, pk):
        blog = get_object_or_404(Blog, id=pk)
        serializer = BlogDetailCommentSerializer(blog)
        return Response({
            "status": "HTTP 200 OK",
            "data": serializer.data
            })

    # 4) 게시글 수정하기 : PATCH /blogs/{blog_id}
    def patch(self, request, pk):
        blog = get_object_or_404(Blog, id=pk)
        serializer = BlogDetailSerializer(blog, data=request.data, partial=True) #제목만 바꾸거나 본문만 바꾸거나 해도 ok
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "HTTP 200 OK",
                "data": serializer.data
                })
        else:
            return Response({
                "status": "HTTP 400 BAD REQUEST",
                "error": serializer.errors
                })

    # 5) 게시글 삭제하기 : DELETE /blogs/{blog_id}
    def delete(self, request, pk):
        blog = get_object_or_404(Blog, id=pk)
        blog.delete()
        return Response({
            "status": "HTTP 204 NO CONTENT"
            })

class CommentListAPIView(APIView):
    # 6) 특정 게시글의 댓글 목록 불러오기 : GET /blogs/{blog_id}/comments/
    def get(self, request, pk):
        comments = Comment.objects.filter(blog_id=pk)
        serializer = CommentSerializer(comments, many=True)
        return Response({
            "status": "HTTP 200 OK",
            "data": serializer.data, 
            })

    # 7) 게시글에 댓글 작성하기 : POST /blogs/{blog_id}/comments/
    def post(self, request, pk):
        blog = get_object_or_404(Blog, id=pk)
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            # 현재 주소창에 있는 blog 객체를 강제로 주입하여 저장
            serializer.save(blog=blog)
            return Response({
                "status": "HTTP 201 CREATED",
                "data": serializer.data, 
                })
        else:
            return Response({
                "status": "HTTP 400 BAD REQUEST",
                "error": serializer.errors
                })

