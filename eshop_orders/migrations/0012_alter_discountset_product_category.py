# Generated by Django 3.2.4 on 2021-12-29 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_product_categories', '0001_initial'),
        ('eshop_orders', '0011_alter_discountset_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discountset',
            name='product_category',
            field=models.ManyToManyField(blank=True, to='eshop_product_categories.ProductCategory'),
        ),
    ]