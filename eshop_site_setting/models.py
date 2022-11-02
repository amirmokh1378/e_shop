from django.db import models


# Create your models here.
class ContactManager(models.Manager):
    def get_active_object(self):
        return self.filter(active=True).first()


class SiteSetting(models.Model):
    name = models.CharField(max_length=200, verbose_name='اسم')
    email = models.EmailField(verbose_name='ایمیل')
    phone_number = models.CharField(max_length=50, verbose_name='شماره مویایل', blank=True)
    company_number = models.CharField(max_length=50, verbose_name='شماره تلفن', blank=True)
    about_us = models.TextField(verbose_name='توضیحات', blank=True)
    track = models.CharField(max_length=300, verbose_name='ادرس', blank=True)
    active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')

    objects = ContactManager()

    class Meta:
        verbose_name = 'تنظیم'
        verbose_name_plural = 'تنظیمات'

    def __str__(self):
        return self.name
