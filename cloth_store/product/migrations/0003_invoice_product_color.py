# Generated by Django 4.0.5 on 2022-06-27 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_remove_sub_products_no_of_purchases_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='product_color',
            field=models.CharField(default='kjdb', max_length=15),
        ),
    ]
