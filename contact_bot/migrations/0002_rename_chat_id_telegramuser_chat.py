# Generated by Django 4.1.4 on 2023-01-02 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_bot', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='telegramuser',
            old_name='chat_id',
            new_name='chat',
        ),
    ]