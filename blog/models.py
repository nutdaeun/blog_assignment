from django.db import models
from accounts.models import CustomUser

class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE) 

    def __str__(self):
        return self.title

class Comment(models.Model):
    # 역참조를 편하게 하기 위해 related_name='comments' 추가
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment[:10]