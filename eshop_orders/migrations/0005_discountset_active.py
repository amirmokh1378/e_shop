# Generated by Django 3.2.4 on 2021-12-29 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_orders', '0004_auto_20211227_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='discountset',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
