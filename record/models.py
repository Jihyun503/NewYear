from django.db import models
from django.core.validators import MaxValueValidator


class Record(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    goal = models.ForeignKey('goal.Goal', on_delete=models.CASCADE)
    practice = models.TextField(verbose_name="실천사항")
    percent = models.SmallIntegerField(verbose_name="달성률", validators=[MaxValueValidator(100)])  # 기록한 날짜 달성률
    record_date = models.DateTimeField(verbose_name="기록날짜")
