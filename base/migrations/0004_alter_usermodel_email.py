# Generated by Django 4.0.2 on 2022-02-22 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_usermodel_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
