# Generated by Django 4.0.4 on 2022-04-27 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_car_customer_order_car_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('process', 'process'), ('done', 'done')], default='unknown', max_length=7),
        ),
    ]
