# Generated by Django 5.1.2 on 2024-10-27 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instgram', '0004_alter_comments_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='name',
            field=models.CharField(default='comments'),
        ),
    ]
