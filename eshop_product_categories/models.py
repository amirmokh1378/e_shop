from django.db import models


# Create your models here.
from django.db.models.signals import pre_save


class ProductCategory(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    name = models.CharField(max_length=200, verbose_name='عنوان در url')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title


def category_pre_save_receiver(sender, instance, *args, **kwargs):
    instance.name = instance.name.replace(' ', '-')


pre_save.connect(category_pre_save_receiver, sender=ProductCategory)
