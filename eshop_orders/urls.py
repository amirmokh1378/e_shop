from django.urls import path
from eshop_orders.views import add_user_order, remove_detail_product, partial_discount_component_view
from .views import order_page, n
from django.urls import path

app_name = 'order'

urlpatterns = [
    path('add_user_order', add_user_order, name='order'),
    path('order', order_page, name='order_page'),
    path('remove/<order_detail_id>', remove_detail_product, name='remove'),
    path('discount', partial_discount_component_view, name='discount')
]

if n == 1:
    from .views import pay_orders, verify

    urlpatterns += [
        path('pay', pay_orders, name='pay'),
        path('verify/<order_id>', verify, name='verify'),
    ]
