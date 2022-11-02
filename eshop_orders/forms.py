from django import forms
from django.core import validators


class UserNewOrderForm(forms.Form):
    product_id = forms.IntegerField(
        widget=forms.HiddenInput(),
    )

    count = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': "search_box", 'placeholder': "تعداد"}),
        label='تعداد',
        validators=[validators.MinValueValidator(0, 'باید تعداد بیشتر از 0 باشد')],
        initial=1
    )


class DiscountForm(forms.Form):
    code = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': "تعداد"}),
        label='کد تخفیف خود را وارد نمایید ...',
    )

# class DiscountSetForm(forms.ModelForm):
#     class Meta:
#         model = DiscountSet
#         fields = ['name', 'count', 'percent']
#
#     def clean(self):
#         newCount = self.cleaned_data['count']
#
#         if newCount < oldCount:
#             raise forms.ValidationError("TEST EXCEPTION!")
