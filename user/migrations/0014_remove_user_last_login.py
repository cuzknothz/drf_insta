# Generated by Django 4.1.7 on 2023-02-25 03:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_alter_user_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='last_login',
        ),
    ]
