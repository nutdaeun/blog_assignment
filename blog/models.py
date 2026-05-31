from django.db import models
from accounts.models import CustomUser

# Create your models here.
'''
class BlogManager(models.Manager):
    def by_user(self, user):
        return self.get_queryset().filter(user=user)
    
    def recent(self, count=10):
        return self.get_queryset().order_by('-date')[:count]
    
    def search(self, keyword):
        return self.get_queryset().filter(title__icontains=keyword)
'''

class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(default="")
    date = models.DateTimeField(auto_now_add=True) # 생성일자를 기준으로 날짜 기록
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE) 

    objects = models.Manager()


    def __str__(self):
        return self.title