# Generated by Django 4.0.4 on 2022-05-01 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_order_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Phone',
            field=models.CharField(max_length=16, verbose_name='Phone Customer'),
        ),
    ]