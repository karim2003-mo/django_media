# Generated by Django 5.1.2 on 2024-10-27 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instgram', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
            ],
        ),
    ]
