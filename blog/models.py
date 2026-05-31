from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(default="")
    date = models.DateTimeField(auto_now_add=True) # 생성일자를 기준으로 날짜 기록
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE) 


    def __str__(self):
        return self.title