# Generated by Django 5.1.6 on 2025-02-18 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0003_package_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='media_files',
            field=models.JSONField(blank=True, default=list, verbose_name='تصاویر و ویدیوها'),
        ),
    ]
