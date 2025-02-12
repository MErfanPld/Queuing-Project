# forms.py
from django import forms
from users.models import User
from django.contrib.auth import authenticate

class UserLoginForm(forms.Form):
    phone_number = forms.CharField(max_length=11, label='شماره موبایل')
    email = forms.EmailField(label='ایمیل', required=False)  # ایمیل اختیاری
    password = forms.CharField(widget=forms.PasswordInput, label='رمز عبور')

    def clean(self):
        cleaned_data = super().clean()
        phone_number = cleaned_data.get("phone_number")
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if not phone_number or not password:
            raise forms.ValidationError("شماره موبایل و رمز عبور الزامی است.")

        # بررسی وجود کاربر
        user = authenticate(phone_number=phone_number, password=password)
        if user is None:
            # اگر کاربر وجود ندارد، کاربر جدید بسازید
            if not email:
                raise forms.ValidationError("برای ثبت‌نام، ایمیل الزامی است.")
            user = User.objects.create_user(phone_number=phone_number, email=email, password=password)
        cleaned_data['user'] = user
        return cleaned_data
