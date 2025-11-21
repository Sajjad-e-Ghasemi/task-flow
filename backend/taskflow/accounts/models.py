from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=150, unique=True, verbose_name="نام کاربری")
    email = models.EmailField(unique=True, verbose_name="ایمیل")
    password = models.CharField(max_length=128, verbose_name="رمز عبور")
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ عضویت")
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name="آواتار")


    def __str__(self):
        return f"{self.username} - {self.email}"

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"
        ordering = ['-date_joined'] 