# Generated by Django 4.1.4 on 2023-01-13 12:26

import ckeditor.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, verbose_name='Created at')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, verbose_name='Created at')),
                ('name', models.CharField(max_length=255, verbose_name='Location Name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='vacancy',
            name='content',
            field=ckeditor.fields.RichTextField(default=123),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vacancy',
            name='name',
            field=models.CharField(default=123, max_length=255, verbose_name='Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vacancy',
            name='on_site_option',
            field=models.BooleanField(default=False, verbose_name='On-Site Option'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='remote_option',
            field=models.BooleanField(default=False, verbose_name='Remote Option'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='category',
            field=models.ForeignKey(default=123, on_delete=django.db.models.deletion.CASCADE, to='core.category', verbose_name='Category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vacancy',
            name='location',
            field=models.ForeignKey(default=123, on_delete=django.db.models.deletion.CASCADE, to='core.location', verbose_name='Location'),
            preserve_default=False,
        ),
    ]