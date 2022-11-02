# Generated by Django 3.2.4 on 2021-09-18 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eshop_products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('slug', models.SlugField(blank=True, verbose_name='عنوان در url')),
                ('active', models.BooleanField(default=True, verbose_name='فعال/غیرفعال')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='زمان ساخت')),
                ('products', models.ManyToManyField(blank=True, to='eshop_products.Product', verbose_name='محصولات')),
            ],
            options={
                'verbose_name': 'تگ',
                'verbose_name_plural': 'تگ ها',
            },
        ),
    ]