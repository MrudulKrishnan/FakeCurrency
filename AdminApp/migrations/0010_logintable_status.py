# Generated by Django 4.2.16 on 2024-10-03 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0009_alter_logintable_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='logintable',
            name='status',
            field=models.CharField(choices=[('DEACTIVE', 'Deactive'), ('ACTIVE', 'Active')], max_length=20, null=True),
        ),
    ]
