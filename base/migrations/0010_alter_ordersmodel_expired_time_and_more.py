# Generated by Django 4.0.2 on 2022-02-21 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_remove_ordersmodel_duration_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordersmodel',
            name='expired_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='ordersmodel',
            name='order_time',
            field=models.TimeField(null=True),
        ),
    ]
