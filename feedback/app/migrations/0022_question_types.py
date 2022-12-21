# Generated by Django 4.1.4 on 2022-12-21 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_remove_question_types'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='types',
            field=models.CharField(choices=[('is_text', 'is_text'), ('is_radio', 'is_radio'), ('is_select', 'is_select'), ('is_date', 'is_date')], default='is_text', max_length=10, verbose_name='Тип'),
        ),
    ]
