# Generated by Django 4.1.4 on 2022-12-17 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_subquestion_options_question_is_radio'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='is_select',
            field=models.BooleanField(default=False, verbose_name='Статус select'),
        ),
        migrations.AlterField(
            model_name='question',
            name='is_radio',
            field=models.BooleanField(default=False, verbose_name='Статус radio'),
        ),
    ]
