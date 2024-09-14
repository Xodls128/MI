from django.db import models

# Create your models here.
####################켈린더에 들어갈 함수모델##########################
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
    
    ####################계산기에 들어갈 함수모델#####################
class GeneralTechnicalScore(models.Model):
    license_score = models.IntegerField(default=0)
    attendance_score = models.IntegerField(default=0)
    interview_score = models.IntegerField(default=0)
    additional_score = models.IntegerField(default=0)

    def total_score(self):
        return self.license_score + self.attendance_score + self.interview_score + self.additional_score

class SpecialTechnicalScore(models.Model):
    license_score = models.IntegerField(default=0)
    major_score = models.IntegerField(default=0)
    attendance_score = models.IntegerField(default=0)
    interview_score = models.IntegerField(default=0)
    additional_score = models.IntegerField(default=0)

    def total_score(self):
        return self.license_score + self.major_score + self.attendance_score + self.interview_score + self.additional_score

############################################