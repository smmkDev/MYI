# Generated by Django 4.1.5 on 2023-05-13 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0012_stats_remove_answer_alumnis_remove_answer_students_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='alumnis',
            new_name='alumni',
        ),
        migrations.RenameField(
            model_name='answer',
            old_name='students',
            new_name='student',
        ),
    ]
