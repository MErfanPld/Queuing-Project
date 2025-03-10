# Generated by Django 5.1 on 2025-02-05 10:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='نام کسب\u200cوکار')),
                ('business_type', models.CharField(choices=[('salon', 'آرایشگاه')], max_length=20, verbose_name='نوع کسب\u200cوکار')),
                ('address', models.CharField(max_length=255, verbose_name='آدرس')),
                ('telephone_number', models.CharField(max_length=15, verbose_name='شماره تلفن')),
                ('phone_number', models.CharField(max_length=15, verbose_name='شماره همراه')),
                ('is_coffee_shop', models.BooleanField(default=False, verbose_name='کافی شاپ دارد؟')),
                ('is_parking', models.BooleanField(default=False, verbose_name='پارکینگ دارد؟')),
                ('instagram_link', models.URLField(verbose_name='لینک اینستاگرام')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='صاحب کسب\u200cوکار')),
            ],
            options={
                'verbose_name': 'کسب\u200cوکار',
                'verbose_name_plural': 'کسب\u200cوکارها',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=255, verbose_name='نام مهارت')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name=' کارمند')),
            ],
            options={
                'verbose_name': 'کارمند',
                'verbose_name_plural': 'کارمندان',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='نام سرویس')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('duration', models.DurationField(help_text='مدت زمان به صورت HH:MM:SS', verbose_name='مدت زمان تقریبی')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='قیمت بیانه')),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='business.business', verbose_name='کسب\u200cوکار')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='business.employee', verbose_name='کارمند')),
            ],
            options={
                'verbose_name': 'سرویس',
                'verbose_name_plural': 'سرویس\u200cها',
            },
        ),
    ]
