from django.contrib import admin
from .models import ContactUs


# Register your models here.
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'subject', 'is_read']
    list_filter = ['is_read']
    list_editable = ['subject', 'is_read']
    search_fields = ['subject', 'text']

    class Meta:
        model = ContactUs


admin.site.register(ContactUs, ContactUsAdmin)
