"""e_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from e_shop import settings
from e_shop.views import (
    home_page,
    partial_footer,
    partial_header,
    email_test_view_page,
    message_test_page,
    partial_home_slide_component
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('footer', partial_footer, name='footer'),
    path('header', partial_header, name='header'),
    path('test-email', email_test_view_page),
    path('test-message', message_test_page),
    path('', include('eshop_account.urls', namespace='account')),
    path('', include('eshop_products.urls', namespace='products')),
    path('', include('Bookstore.urls', namespace='bookstore')),
    path('', include('eshop_contact.urls', namespace='contact')),
    path('home_slider', partial_home_slide_component, name='slider'),
    path('', include('eshop_orders.urls', namespace='order')),
    path('', include('eshop_Comments.urls', namespace='comments')),
]

# handler404 = 'e_shop.views.handle_404_errors'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
