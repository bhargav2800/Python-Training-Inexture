# Generated by Django 4.0.6 on 2022-07-21 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='return_replace_days',
            field=models.IntegerField(default=0),
        ),
    ]
