# Generated by Django 5.1.2 on 2024-11-02 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instgram', '0008_users_man_users_operating_system_users_owener_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='account_problem',
            field=models.BooleanField(default=False),
        ),
    ]