# Generated by Django 3.1 on 2020-08-06 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_city_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.CharField(default='https://undark.org/wp-content/uploads/2020/02/GettyImages-1199242002-1-scaled.jpg', max_length=1000),
        ),
    ]