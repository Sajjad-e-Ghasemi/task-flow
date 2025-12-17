from django.db import models
from django.utils import timezone
from accounts.models import Account

def in_30_days():
    pass

class TaskModel(models.Model):
    task_title = models.CharField(max_length=500, verbose_name="نام وظیفه")
    task_desc = models.TextField(verbose_name="توضیحات وظایف")
    task_author = models.ForeignKey(Account, on_delete=models.CASCADE)
    task_started_at = models.DateTimeField(
        verbose_name="تاریخ شروع وظیفه",
        null=True,
        editable=False
    )
    task_ended_at = models.DateTimeField(
        verbose_name="تاریخ پایان وظیفه",
        null=True
    )
    is_done = models.BooleanField(default=False, verbose_name="انجام شده/نشده")

    def __str__(self):
        return f"{self.task_title} / {self.is_done}"
