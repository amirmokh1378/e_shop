# Generated by Django 3.2.4 on 2021-12-15 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_Comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='Score',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2, max_length=5),
        ),
    ]
