# Generated by Django 4.0.2 on 2022-02-09 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idrequestApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='facultytable',
            name='date',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='studenttable',
            name='date',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
