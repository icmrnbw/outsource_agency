# Generated by Django 4.1.4 on 2023-01-13 10:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_bot', '0005_alter_telegramuser_chat_alter_telegramuser_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramuser',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Created at'),
        ),
    ]
