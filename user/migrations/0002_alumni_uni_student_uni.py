# Generated by Django 4.1.5 on 2023-04-22 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumni',
            name='uni',
            field=models.CharField(default='Ned', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='uni',
            field=models.CharField(default='Ned', max_length=50, null=True),
        ),
    ]