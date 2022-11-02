from django.db import models

# Create your models here.

class ContactUs(models.Model):
    full_name = models.CharField(max_length=30, verbose_name='عنوان')
    subject = models.CharField(max_length=150, verbose_name='عنوان')
    text = models.TextField(max_length=1000, verbose_name='توضیحات')
    email = models.EmailField(verbose_name='توضیحات')
    is_read = models.BooleanField(default=False, verbose_name='خواند شده/ خواند نشده')

    class Meta:
        verbose_name = 'تماس'
        verbose_name_plural = 'تماس ها'

    def __str__(self):
        return self.subject

