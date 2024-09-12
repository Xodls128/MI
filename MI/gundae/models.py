from django.db import models

# Create your models here.
class RecruitmentEvent(models.Model):
    군별 = models.CharField(max_length=100)
    모집분야 = models.CharField(max_length=100)
    접수기간 = models.CharField(max_length=100, blank=True, null=True)
    일차합격자발표 = models.CharField(max_length=100, blank=True, null=True)
    최종합격자발표 = models.CharField(max_length=100, blank=True, null=True)
    입영월 = models.CharField(max_length=100, blank=True, null=True)
    모집인원 = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.군별} - {self.모집분야}"