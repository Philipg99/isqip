# Generated by Django 2.0.7 on 2018-07-17 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0006_auto_20180717_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='location',
            field=models.TextField(),
        ),
    ]