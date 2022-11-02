from django.db import models


# Create your models here.

class Comment(models.Model):
    full_name = models.CharField(max_length=20, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(max_length=100, verbose_name='ایمیل')
    description = models.TextField(max_length=500, verbose_name='توضیحات')
    Score = models.DecimalField(max_length=5, max_digits=2, decimal_places=1, default=0, verbose_name='امتیاز')

    def __str__(self):
        return self.full_name
