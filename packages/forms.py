from django import forms
from .models import Package, Service


class PackageForm(forms.ModelForm):
    services = forms.ModelMultipleChoiceField(
        queryset=Service.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="انتخاب سرویس‌ها"
    )

    class Meta:
        model = Package
        fields = ['business', 'name', 'services', 'desc',
                  'total_price', 'image', 'media_files']
