# Generated by Django 4.0.3 on 2022-05-27 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idrequestApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studenttable',
            name='date',
        ),
        migrations.AlterField(
            model_name='studenttable',
            name='idpic',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
        migrations.AlterField(
            model_name='studenttable',
            name='signature',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
    ]