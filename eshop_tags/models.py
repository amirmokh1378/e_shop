from django.db import models
from django.db.models.signals import pre_save
from eshop_tags.utils import unique_slug_generator
from eshop_products.models import Product

# Create your models here.


class Tag(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    slug = models.SlugField(blank=True, verbose_name='عنوان در url')
    active = models.BooleanField(default=True, verbose_name='فعال/غیرفعال')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='زمان ساخت')
    products = models.ManyToManyField(Product, blank=True, verbose_name='محصولات')

    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ ها'

    def __str__(self):
        return self.title


def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    print('slug: ', instance.slug)
    if not instance.slug:
        instance.slug = 'asc'
        instance.slug = unique_slug_generator(instance)


pre_save.connect(tag_pre_save_receiver, sender=Tag)
