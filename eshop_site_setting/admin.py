from django.contrib import admin
from .models import SiteSetting


# Register your models here.

class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'name', 'active']

    class Meta:
        model = SiteSetting


admin.site.register(SiteSetting, SiteSettingAdmin)
