# Generated by Django 3.0.6 on 2020-07-13 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SPORT', '0003_auto_20200713_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ManyToManyField(to='SPORT.Image'),
        ),
    ]
