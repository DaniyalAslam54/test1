# Generated by Django 3.2.8 on 2021-11-06 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20211103_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='earn_from_ads',
            field=models.IntegerField(default=0),
        ),
    ]