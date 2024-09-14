# calculator/models.py
from django.db import models

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

