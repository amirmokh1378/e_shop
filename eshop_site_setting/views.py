from django.shortcuts import render
from .models import SiteSetting

# Create your views here.

siteSettingObject = lambda: SiteSetting.objects.get_active_object()
