from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from eshop_sliders.models import Slider
from eshop_site_setting.views import siteSettingObject
from eshop_products.views import Product, chunks


def home_page(request):
    the_latest_products = Product.objects.order_by('-id')[:8]
    the_most_product_views = Product.objects.order_by('-views_number')[:8]
    the_latest_products_list = chunks(the_latest_products, 4)
    the_most_product_views_list = chunks(the_most_product_views, 4)

    context = {
        'the_latest_products_list': the_latest_products_list,
        'the_most_product_views_list': the_most_product_views_list,
    }
    return render(request, 'home.html', context=context)





# Footer code behind
def partial_footer(request, *args, **kwargs):
    context = {
        'about_us': siteSettingObject().about_us
    }
    return render(request, 'shared/Footer.html', context=context)


def partial_header(request, *args, **kwargs):
    context = {
        'data': 'this build by django '
    }
    return render(request, 'shared/Header.html', context=context)


def partial_home_slide_component(request, *args, **kwargs):
    qu = Slider.objects.get_queryset()
    context = {
        'sliders': qu
    }
    return render(request, 'home_slider_component.html', context=context)


def email_test_view_page(request):
    send_mail(
        'subject',
        ' text',
        'mokh09103791346@gmail.com',
        ['caveko4564@100xbit.com', 'holegok165@697av.com', 'tojiham510@ailoki.com'],
        fail_silently=False,
    )

    context = {

    }
    return render(request, 'test.html', context=context)


def message_test_page(request):
    messages.add_message(request, messages.INFO, 'Hello world.')
    messages.info(request, 'Three credits remain in your account.')
    messages.success(request, 'Profile details updated.')
    messages.warning(request, 'Your account expires in three days.')
    messages.error(request, 'Document deleted.')
    context = {

    }
    return render(request, 'test.html', context=context)


# def handle_404_errors(request, exception):
#     context = {
#
#     }
#     return render(request, 'shared/404.html', context=context)