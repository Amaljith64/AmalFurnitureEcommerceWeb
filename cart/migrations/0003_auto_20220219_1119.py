# Generated by Django 2.2 on 2022-02-19 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20220216_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartlist',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
