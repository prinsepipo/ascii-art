# Generated by Django 2.2.6 on 2019-10-13 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_converter', '0003_delete_convertedimagefile'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsciiImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='raw/')),
                ('ascii_characters', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='RawImageFile',
        ),
    ]