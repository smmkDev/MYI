# Generated by Django 4.1.5 on 2023-05-08 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alumni_banner_image_student_banner_image'),
        ('groups', '0007_remove_post_user_post_post_alm_post_post_std'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='students',
            field=models.ManyToManyField(to='user.student'),
        ),
    ]
