# Generated by Django 5.1.2 on 2024-10-27 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instgram', '0003_operator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.JSONField(default={'comments': []}),
        ),
    ]