# Generated by Django 3.2.7 on 2021-09-30 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hoodapp', '0006_neighhood_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neighhood',
            name='admin',
        ),
    ]
