# Generated by Django 4.1.4 on 2022-12-17 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_subquestion_is_radio_activate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subquestion',
            name='is_radio_activate',
        ),
        migrations.AddField(
            model_name='question',
            name='is_radio_activate',
            field=models.BooleanField(default=False, verbose_name='Статус активатора radio'),
        ),
    ]
