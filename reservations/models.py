from django.db import models
from users.models import User
from business.models import Service, Business
from extenstions.utils import jalali_converter
from business.models import Employee


class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'در انتظار'),
        ('confirmed', 'تایید شده'),
        ('canceled', 'لغو شده'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='appointments', verbose_name="کاربر")
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name='appointments', verbose_name="سرویس")
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True,
                                 null=True, related_name='appointments', verbose_name="کارمند")
    date = models.DateField(verbose_name="تاریخ")
    time = models.TimeField(verbose_name="زمان")
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='pending', verbose_name="وضعیت")

    class Meta:
        verbose_name = "نوبت"
        verbose_name_plural = "نوبت‌ها"

    def __str__(self):
        return f"{self.user} - {self.service} در {self.date} ساعت {self.time}"

    @property
    def get_status(self):
        return dict(self.STATUS_CHOICES).get(self.status, '')


class Schedule(models.Model):
    business = models.ForeignKey(
        Business, on_delete=models.CASCADE, related_name='schedules', verbose_name="کسب‌وکار")
    day_of_week = models.CharField(max_length=10, choices=[
        ('Monday', 'دوشنبه'),
        ('Tuesday', 'سه‌شنبه'),
        ('Wednesday', 'چهارشنبه'),
        ('Thursday', 'پنج‌شنبه'),
        ('Friday', 'جمعه'),
        ('Saturday', 'شنبه'),
        ('Sunday', 'یکشنبه'),
    ], verbose_name="روز هفته")
    start_time = models.TimeField(verbose_name="زمان شروع")
    end_time = models.TimeField(verbose_name="زمان پایان")

    class Meta:
        verbose_name = "زمانبندی"
        verbose_name_plural = "زمانبندی‌ها"

    def __str__(self):
        return f"{self.business.name} - {self.day_of_week}: {self.start_time} تا {self.end_time}"
