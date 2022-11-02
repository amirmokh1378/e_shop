from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save

from eshop_product_categories.models import ProductCategory
import os


# Create your models here.

# import os
# import random
#
#
# def get_filename_ext(filepath):
#     #   base_name = os.path.basename(filepath)
#     #    name, ext = os.path.splitext(base_name)
#     name, ext = os.path.splitext(filepath)
#     print('filepath:', filepath, 'name:', name, 'ext:', ext, sep=" ")
#     return name, ext
#
#
# def upload_image_path(instance, filename):
#     name, ext = get_filename_ext(filename)
#     return f'product/{random.randint(1, 5)}/{instance}.{ext[1:]}'


def product_image_directory_path(instance, filename):
    baseName, ext = os.path.splitext(filename)
    return f'products/{instance}/{instance}{ext}'


def gallery_image_directory_path(instance, filename):
    baseName, ext = os.path.splitext(filename)
    return f'products/galleries/{instance.product}/{instance}{ext}'


class ProductManager(models.Manager):

    def filter_by_gallery(self, product_id):
        qu = ProductGallery.objects.filter(product_id=product_id)
        return qu

    def filter_by_active(self):
        return self.filter(active=True)

    def filter_by_category(self, categoryName):
        qu = ProductCategory.objects.filter(name=categoryName)
        if qu.exists():
            return self.filter(categories__name=categoryName, active=True)
        raise EOFError

    def filter_by_title_or_description(self, item):
        lookup = (
                Q(description__icontains=item) |
                Q(title__icontains=item) |
                Q(tag__title__icontains=item)
        )
        print(lookup)
        qu = self.filter(tag__title__icontains='p')
        print('tag.products: ')
        print('qu: ', qu)
        print('q: ', self.get_queryset().filter(lookup, active=True).distinct().all())
        qu = self.filter(lookup, active=True).distinct()
        return qu


class Query(models.query.QuerySet):
    pass


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    price = models.IntegerField(verbose_name='قیمت')
    image = models.ImageField(upload_to=product_image_directory_path, blank=True, null=True, verbose_name='عکس')
    active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')
    categories = models.ManyToManyField(ProductCategory, blank=True, verbose_name='دسته بندی محصولات')
    views_number = models.IntegerField(default=0, verbose_name='تعداد بازدید')

    objects = ProductManager()

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/products/product/{self.pk}/{self.title.replace(" ", "-")}'


class ViewedProduct(models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='شخص بازدید کننده')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول مشاهده شده')
    is_seen = models.IntegerField(default=0, verbose_name='وضعیت مشاهده')


class ProductGallery(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    image = models.ImageField(upload_to=gallery_image_directory_path, verbose_name='عکس')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')

    class Meta:
        verbose_name = 'گالری'
        verbose_name_plural = 'گالری ها'

    def __str__(self):
        return self.title


def ProductGallery_pre_save_receiver(sender, instance, *args, **kwargs):
    print('instance.product: ', instance.product)


pre_save.connect(ProductGallery_pre_save_receiver, sender=ProductGallery)
