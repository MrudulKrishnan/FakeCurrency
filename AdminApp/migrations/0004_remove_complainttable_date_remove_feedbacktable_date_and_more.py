# Generated by Django 4.2.16 on 2024-09-14 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0003_alter_complainttable_is_active_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complainttable',
            name='Date',
        ),
        migrations.RemoveField(
            model_name='feedbacktable',
            name='Date',
        ),
        migrations.RemoveField(
            model_name='notificationtable',
            name='Date',
        ),
        migrations.RemoveField(
            model_name='worktable',
            name='Date',
        ),
    ]
