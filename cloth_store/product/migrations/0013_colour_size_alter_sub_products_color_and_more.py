# Generated by Django 4.0.5 on 2022-07-09 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_alter_invoice_pick_up_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colour', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='sub_products',
            name='color',
            field=models.CharField(default='red', max_length=10),
        ),
        migrations.AlterField(
            model_name='sub_products',
            name='size',
            field=models.CharField(default='XL', max_length=10),
        ),
    ]
