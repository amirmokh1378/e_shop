from django.shortcuts import render
from .models import ContactUs
from .forms import ContactUsForm
from eshop_site_setting.views import siteSettingObject

# Create your views here.
def contact_us_page(request):
    form = ContactUsForm(request.POST or None)
    context = {
        'phone_number': siteSettingObject().phone_number,
        'company_number': siteSettingObject().company_number,
        'track': siteSettingObject().track,
        'email': siteSettingObject().email,
        'name': siteSettingObject().name,
        'form': form,
    }
    if form.is_valid():
        subject = form.cleaned_data.get('subject')
        email = form.cleaned_data.get('email')
        explaining = form.cleaned_data['explaining']
        full_name = form.cleaned_data.get('full_name')
        ContactUs.objects.create(subject=subject, email=email, text=explaining, full_name=full_name, is_read=False)
        context['form'] = ContactUsForm()
        context['text'] = 'با موفقیت انجام شد'
        # objectModel = ContactUs(subject=subject, email=email, text=explaining, full_name=full_name)
        # objectModel.save()

    return render(request, 'contact_us/contact_us_page.html', context=context)
