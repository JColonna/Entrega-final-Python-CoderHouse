# Generated by Django 3.2.9 on 2022-01-10 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appfinal', '0002_indumentaria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='indumentaria',
            name='hayStock',
        ),
        migrations.RemoveField(
            model_name='indumentaria',
            name='talle',
        ),
        migrations.AlterField(
            model_name='indumentaria',
            name='tipo',
            field=models.CharField(max_length=40),
        ),
    ]
