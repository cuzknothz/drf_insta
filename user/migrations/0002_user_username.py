# Generated by Django 4.1.7 on 2023-02-24 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='fd', max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
