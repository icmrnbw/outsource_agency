# Generated by Django 4.1.3 on 2023-01-24 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_category_vacancycategory_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancy',
            name='category',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='location',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.DeleteModel(
            name='Vacancy',
        ),
        migrations.DeleteModel(
            name='VacancyCategory',
        ),
    ]