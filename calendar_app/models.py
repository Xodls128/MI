# models.py

from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    announcement_date = models.DateField(blank=True, null=True)  # 합격발표일 필드 추가
    backgroundColor = models.CharField(max_length=7, default='#3788d8')  # HEX 코드 색상 필드
    applyUrl = models.CharField(max_length= 200)

    def __str__(self):
        return self.title
