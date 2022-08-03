# Generated by Django 4.0.5 on 2022-06-28 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_order_payment_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.IntegerField(choices=[(1, 'Not Packed'), (2, 'Ready For Shipment'), (3, 'Shipped'), (4, 'Delivered')], default=1),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_status',
            field=models.IntegerField(choices=[(1, 'SUCCESS'), (2, 'FAILURE'), (3, 'PENDING')], default=3),
        ),
        migrations.AddField(
            model_name='order',
            name='razorpay_order_id',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='razorpay_payment_id',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='razorpay_signature',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
