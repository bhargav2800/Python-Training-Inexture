# Generated by Django 4.0.5 on 2022-07-05 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_invoice_order_delivery_date_invoice_pick_up_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='order_delivery_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]