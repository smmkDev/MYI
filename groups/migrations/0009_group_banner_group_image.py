# Generated by Django 4.1.5 on 2023-05-09 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0008_group_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='banner',
            field=models.ImageField(null=True, upload_to='group_images/banners'),
        ),
        migrations.AddField(
            model_name='group',
            name='image',
            field=models.ImageField(null=True, upload_to='group_images/main_images'),
        ),
    ]
