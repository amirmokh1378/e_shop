# Generated by Django 3.2.4 on 2021-09-18 15:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eshop_products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_paid', models.BooleanField(verbose_name='پرداخت شده/نشده')),
                ('payment_data', models.DateTimeField(blank=True, null=True, verbose_name='تاریخ پرداخت')),
                ('confirmed_code', models.CharField(blank=True, max_length=100, null=True, verbose_name='کد پیگیری')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='صاحب سبد')),
            ],
            options={
                'verbose_name': 'سفارش',
                'verbose_name_plural': 'سفارشات',
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='تعداد محصول')),
                ('price', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='قیمت کل تومان')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop_orders.order', verbose_name='سبد خرید')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop_products.product', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'جزیات سفارش',
                'verbose_name_plural': 'جزیات سفارشات',
            },
        ),
    ]
