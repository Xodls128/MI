# models.py

from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)  # 추가적인 설명 필드
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    color = models.CharField(max_length=7, default='#3788d8')  # HEX 코드 색상 필드
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
