# Generated by Django 3.2.9 on 2022-12-19 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20221219_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subquestion',
            name='name',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='name'),
        ),
    ]
