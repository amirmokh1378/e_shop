# Generated by Django 3.2.4 on 2021-12-27 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_orders', '0002_discount_discountset'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discount',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='discount',
            name='expiration_date',
        ),
        migrations.RemoveField(
            model_name='discount',
            name='percent',
        ),
    ]
