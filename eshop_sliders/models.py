import os

from django.db import models


# Create your models here.
def slider_image_directory_path(instance, filename):
    baseName, ext = os.path.splitext(filename)
    return f'slider/{instance}/{instance}{ext}'


class Slider(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    link = models.URLField(max_length=300, verbose_name='ادرس')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to=slider_image_directory_path, verbose_name='عکس')

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدرها'

    def __str__(self):
        return self.title
