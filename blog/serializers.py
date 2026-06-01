from rest_framework import serializers
from blog.models import Blog, Comment

# 블로그 글 목록 조회 GET blogs/
class BlogListSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = Blog
        fields = ["id", "title", "body", "created_at"]
    
# 블로그 글 쓰기 POST blogs/ 및 수정 PATCH blogs/{id}/
class BlogDetailSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = Blog
        fields = ["id", "title", "body", "created_at"]

# 댓글 조회 GET blogs/{int:pk}/comments 및 댓글 작성
class CommentSerializer(serializers.ModelSerializer):
    # Comment 모델의 blog 객체에서 id를 추출해 'blog_id'라는 Key로 출력
    blog_id = serializers.ReadOnlyField(source='blog.id')
    created_at = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "blog_id", "comment", "created_at"] 

# 블로그 글 상세 조회 GET blogs/{int:pk} (글 + 댓글 함께 조회)
class BlogDetailCommentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Blog
        fields = ["id", "title", "body", "created_at", "comments"]
