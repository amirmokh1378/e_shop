# Generated by Django 3.2.4 on 2021-12-25 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscountSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('count', models.IntegerField()),
                ('percent', models.IntegerField()),
                ('cost', models.DecimalField(decimal_places=0, max_digits=2)),
                ('expiration_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('expiration_date', models.DateTimeField()),
                ('use_date', models.DateTimeField(blank=True, null=True)),
                ('active', models.BooleanField(blank=True, null=True)),
                ('percent', models.IntegerField()),
                ('cost', models.DecimalField(decimal_places=0, max_digits=10)),
                ('discount_set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop_orders.discountset')),
            ],
        ),
    ]
