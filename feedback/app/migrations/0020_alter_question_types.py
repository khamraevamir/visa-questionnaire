# Generated by Django 4.1.4 on 2022-12-21 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_remove_question_is_radio_remove_question_is_select_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='types',
            field=models.CharField(choices=[('is_text', 'is_text'), ('is_radio', 'is_radio'), ('is_select', 'is_select'), ('is_date', 'is_date')], default='is_text', max_length=10, verbose_name='Тип'),
        ),
    ]
