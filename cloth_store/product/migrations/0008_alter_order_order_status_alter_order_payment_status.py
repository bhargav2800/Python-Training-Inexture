# Generated by Django 4.0.5 on 2022-06-29 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_order_order_id_order_order_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('Not Packed', 'Not Packed'), ('Ready For Shipment', 'Ready For Shipment'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered')], default='Not Packed', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.CharField(choices=[('SUCCESS', 'SUCCESS'), ('FAILURE', 'FAILURE'), ('PENDING', 'PENDING')], default='PENDING', max_length=20),
        ),
    ]
