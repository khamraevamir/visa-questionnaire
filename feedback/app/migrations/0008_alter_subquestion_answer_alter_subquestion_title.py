# Generated by Django 4.1.4 on 2022-12-17 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_subquestion_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subquestion',
            name='answer',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ответ'),
        ),
        migrations.AlterField(
            model_name='subquestion',
            name='title',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Подвопрос'),
        ),
    ]
