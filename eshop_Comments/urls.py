from django.urls import path

from .views import (
    comments_view

)

app_name = "eshop_comments"

urlpatterns = [
    path('comment', comments_view, name='comment'),
]
