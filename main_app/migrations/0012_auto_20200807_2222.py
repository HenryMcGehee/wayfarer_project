# Generated by Django 3.1 on 2020-08-07 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_auto_20200807_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=5000, verbose_name=''),
        ),
    ]