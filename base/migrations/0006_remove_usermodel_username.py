# Generated by Django 4.0.2 on 2022-02-22 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_usermodel_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='username',
        ),
    ]