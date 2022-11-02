from django.urls import path

from eshop_account.views import login_page, register_page, logout_user

app_name = "eshop_account"

urlpatterns = [
    path('login', login_page, name='login'),
    path('logout', logout_user, name='logout'),
    path('register', register_page, name='register'),
]
