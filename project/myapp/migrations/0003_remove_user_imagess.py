# Generated by Django 5.1.2 on 2024-10-30 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_user_imagess_alter_request_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='imagess',
        ),
    ]
