from django.contrib import admin
from eshop_sliders.models import Slider


# Register your models here.

class SliderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'link', 'image']

    class Meta:
        model = Slider


admin.site.register(Slider, SliderAdmin)
