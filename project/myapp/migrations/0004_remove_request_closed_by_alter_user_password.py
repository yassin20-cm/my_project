# Generated by Django 5.1.2 on 2024-10-30 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_user_imagess'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='closed_by',
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
