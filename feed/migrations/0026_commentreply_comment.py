# Generated by Django 4.1.7 on 2023-03-11 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0025_remove_comment_reply_commentcommentreply_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentreply',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='feed.comment'),
        ),
    ]
