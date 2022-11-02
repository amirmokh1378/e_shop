from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.timezone import now

from eshop_products.models import Product
from .forms import UserNewOrderForm, DiscountForm
from .models import Order, OrderDetail, Discount

from django.http import HttpResponse, Http404
from zeep import Client


# Create your views here.


@login_required(login_url='/login')
def add_user_order(request):
    new_order_form = UserNewOrderForm(request.POST or None)

    if new_order_form.is_valid():
        owner_id = request.user.id
        product_id = new_order_form.cleaned_data.get('product_id')
        count = new_order_form.cleaned_data['count']
        productPrice = Product.objects.filter(pk=product_id).first().price
        price = productPrice
        order = Order.objects.filter(is_paid=False, owner__id=owner_id)
        if order.exists():
            order = order.first()
            orderDetail = OrderDetail(order=order, product_id=product_id, count=count, price=price)
            orderDetail.save()
        else:
            order = Order.objects.create(owner_id=owner_id, is_paid=False)
            print(order)
            # order.orderdetail_set.create()
            OrderDetail.objects.create(order=order, product_id=product_id, count=count, price=price)

    return redirect(
        f'products/product/{request.POST["product_id"]}/{request.POST.get("product_name").replace(" ", "-")}')


@login_required(login_url='/login')
def order_page(request):
    owner_id = request.user.id
    order = Order.objects.filter(owner_id=owner_id, is_paid=False).first()
    order_products = OrderDetail.objects.filter(order=order)

    context = {
        'order_products': order_products,
    }
    return render(request, 'order/order_page.html', context=context)


# @login_required(login_url='/login')
# def add_user_order(request):
#     new_order_form = UserNewOrderForm(request.POST or None)
#
#     if new_order_form.is_valid():
#         order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
#         if order is None:
#             order = Order.objects.create(owner_id=request.user.id, is_paid=False)
#
#         product_id = new_order_form.cleaned_data.get('product_id')
#         count = new_order_form.cleaned_data.get('count')
#         if count < 0:
#             count = 1
#         product = Product.objects.get_by_id(product_id=product_id)
#         order.orderdetail_set.create(product_id=product.id, price=product.price, count=count)
#         # todo: redirect user to user panel
#         # return redirect('/user/orders')
#         return redirect(f'/products/{product.id}/{product.title.replace(" ", "-")}')
#
#     return redirect('/')


# @login_required(login_url='/login')
# def user_open_order(request):
#     context = {
#         'order': None,
#         'details': None
#     }
#
#     open_order: Order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
#     if open_order is not None:
#         context['order'] = open_order
#         context['details'] = open_order.orderdetail_set.all()
#
#     return render(request, 'order/user_open_order.html', context)


def remove_detail_product(request, *args, **kwargs):
    order_detail_id = kwargs['order_detail_id']
    print(request, order_detail_id)
    owner_id = request.user.id
    order_details = OrderDetail.objects.filter(id=order_detail_id, order__owner=owner_id)
    print(order_details)
    order_detail: OrderDetail = order_details.first()
    if order_details.first():
        print(order_detail.delete())
    return redirect('/order')


MERCHANT = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
amount = 0  # Toman / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
email = 'email@example.com'  # Optional
mobile = '09123456789'  # Optional

client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
CallbackURL = 'http://localhost:8000/verify'  # Important: need to edit for realy server.

n = 1

if n == 1:
    @login_required(login_url='/login')
    def pay_orders(request):
        owner_id = request.user.id
        open_order: Order = Order.objects.filter(owner_id=owner_id, is_paid=False).first()
        if open_order is not None:
            amount = open_order.get_complete_price()
            result = client.service.PaymentRequest(MERCHANT, amount, description, email, mobile,
                                                   f'{CallbackURL}/{open_order.id}')
            if result.Status == 100:
                return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
            else:
                return HttpResponse('Error code: ' + str(result.Status))
        raise Http404('سبد خریدی وجود ندارد')


    def verify(request, order_id: Order):
        if request.GET.get('Status') == 'OK':
            result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
            if result.Status == 100:
                open_order: Order = Order.objects.filter(order_id=order_id, is_paid=False).first()
                open_order.is_paid = True
                open_order.payment_data = now()
                open_order.confirmed_code = f'{result.RefID}'
                open_order.save()
                return HttpResponse('Transaction success.\nRefID: ' + str(result.RefID))
            elif result.Status == 101:
                return HttpResponse('Transaction submitted : ' + str(result.Status))
            else:
                return HttpResponse('Transaction failed.\nStatus: ' + str(result.Status))
        else:
            return HttpResponse('Transaction failed or canceled by user')


# discount
def partial_discount_component_view(request):
    discount_form = DiscountForm(request.POST or None)

    context = {
        'discount_form': discount_form,
    }
    if discount_form.is_valid():
        code = discount_form.cleaned_data.get('code')
        discount = Discount.objects.get(code=code)
        if discount is not None:
            pass

    return render(request, template_name='order/discount_component.html', context=context)
