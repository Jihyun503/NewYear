from django.db import models


class Goal(models.Model):
    bno = models.AutoField(primary_key=True)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    goal = models.CharField(max_length=64, verbose_name="목표명")
    contents = models.TextField(verbose_name="내용")
    start_date = models.DateTimeField(verbose_name="시작날짜")
    percent = models.SmallIntegerField(default=0, verbose_name="달성률")
