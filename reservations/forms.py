from django import forms
from .models import Appointment
from business.models import Service


class AppointmentForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),label="تاریخ رزرو")
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}), label="زمان رزرو")
    service = forms.ModelChoiceField(queryset=Service.objects.all(), label="سرویس",
                                     empty_label="لطفاً یک سرویس انتخاب کنید")

    class Meta:
        model = Appointment
        fields = ['service', 'date', 'time']


class UpdateAppointmentStatusForm(forms.Form):
    status = forms.ChoiceField(choices=[
        ('pending', 'در انتظار'),
        ('confirmed', 'تایید شده'),
        ('canceled', 'لغو شده')
    ])
