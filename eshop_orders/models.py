from django.db import models, connection
from django.contrib.auth.models import User
from django.db.models import Max
from eshop_products.models import Product, ProductCategory
from django.core.exceptions import ValidationError
import random
import string
from django import forms


# Create your models here.


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='صاحب سبد')
    is_paid = models.BooleanField(verbose_name='پرداخت شده/نشده')
    payment_data = models.DateTimeField(blank=True, null=True, verbose_name='تاریخ پرداخت')
    confirmed_code = models.CharField(max_length=100, null=True, blank=True, verbose_name='کد پیگیری')

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات'

    def __str__(self):
        return self.owner.username

    def get_complete_price(self):
        totalPrice = 0
        for orderDetail in self.orderdetail_set.all():
            totalPrice += orderDetail.get_total_price()
        return totalPrice


class OrderDetail(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name='محصول')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سبد خرید')
    count = models.IntegerField(verbose_name='تعداد محصول')
    price = models.DecimalField(decimal_places=2, max_digits=15, verbose_name='قیمت کل تومان', )

    class Meta:
        verbose_name = 'جزیات سفارش'
        verbose_name_plural = 'جزیات سفارشات'

    def __str__(self):
        return self.product.title

    def get_total_price(self):
        return self.price * self.count


class DiscountSet(models.Model):
    name = models.CharField(max_length=100)
    count = models.IntegerField()
    percent = models.IntegerField()
    cost = models.DecimalField(decimal_places=0, max_digits=2)
    expiration_date = models.DateTimeField()
    active = models.BooleanField(default=False)
    product_category = models.ManyToManyField(ProductCategory, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.id is None:
            id__max = DiscountSet.objects.aggregate(Max('id'))['id__max']
            if id__max is None:
                id__max = 0
            self.id = id__max + 1
            for num in range(self.count):
                discount = Discount(code=random_char(), discount_set=self, )
                discount.save()

        else:
            newCount = self.count
            oldCount = DiscountSet.objects.get(id=self.id).count
            count = newCount - oldCount
            for num in range(count):
                discount = Discount(code=random_char(), discount_set=self, )
                discount.save()

        return super(DiscountSet, self).save(*args, **kwargs)

    def clean(self, *args, **kwargs):
        if self.id is not None:
            newCount = self.count
            oldCount = DiscountSet.objects.get(id=self.id).count
            if newCount < oldCount:
                raise ValidationError(f"تعداد کمتر از مقدار قدیمی می باشد, \n باید بزرگتر یا {oldCount} باشد")
        return super(DiscountSet, self).clean(*args, **kwargs)


class Discount(models.Model):
    code = models.CharField(max_length=50)
    discount_set = models.ForeignKey(DiscountSet, on_delete=models.CASCADE)
    use_date = models.DateTimeField(blank=True, null=True)
    use = models.BooleanField(blank=True, null=True, default=False)


def random_char(y=10):
    return ''.join(
        str(random.choice(list(string.ascii_letters) + [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, '_'])) for x in range(y))

# this save is for model
# def save(self, *args, **kwargs):
# if self.id is None:
#     id__max = DiscountSet.objects.aggregate(Max('id'))['id__max']
#     if id__max is None:
#         id__max = 0
#     self.id = id__max + 1
#     for num in range(self.count):
#         discount = Discount(code=random_char(), discount_set=self,)
#         discount.save()
#
# else:
#     newCount = self.count
#     oldCount = DiscountSet.objects.filter(id=self.id)
#     count = newCount - oldCount
#     discount_set_qu = self.discount_set.all().filter(use=False)
#     if count > 0:
#         numDSs = discount_set_qu.count()
#         for numDS in range(numDSs):
#             discount_set_qu[numDS].update(percent=self.percent, expiration_date=self.expiration_date)
#         for num in range(self.count):
#             discount = Discount(code=random_char(), discount_set=self, expiration_date=self.expiration_date)
#             discount.save()
#     elif count < 0:
#         raise ValueError('count<0')
#     else:
#         numDSs = discount_set_qu.count()
#         for numDS in range(numDSs):
#             discount_set_qu[numDS].update(percent=self.percent,
#                                           expiration_date=self.expiration_date)
#     discount_set_qu = self.discount_set.all()
#     print('this is discount_set_qu: ', discount_set_qu)
#
# # def my_custom_sql():
# #     with connection.cursor() as cursor:
# #         cursor.execute(
# #             f"CREATE VIEW [Brazil Customers] AS SELECT * FROM eshop_orders_discountset")
# #         cursor.execute(f"SELECT * FROM [Brazil Customers] ")
# #         row = cursor.fetchall()
# #
# #     return row
# #
# # print('sql: ', my_custom_sql())
#
# return super(DiscountSet, self).save(*args, **kwargs)
