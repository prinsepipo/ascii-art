# Generated by Django 2.2.6 on 2019-10-13 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_converter', '0004_auto_20191013_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asciiimage',
            name='ascii_characters',
            field=models.CharField(max_length=200),
        ),
    ]