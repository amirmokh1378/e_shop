# Generated by Django 3.2.4 on 2021-12-29 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_product_categories', '0001_initial'),
        ('eshop_orders', '0010_alter_discountset_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discountset',
            name='product_category',
            field=models.ManyToManyField(null=True, to='eshop_product_categories.ProductCategory'),
        ),
    ]