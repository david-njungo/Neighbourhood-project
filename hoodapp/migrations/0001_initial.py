# Generated by Django 3.2.7 on 2021-09-30 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Neighhood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hoodname', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('occupantscount', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['hoodname'],
            },
        ),
    ]
