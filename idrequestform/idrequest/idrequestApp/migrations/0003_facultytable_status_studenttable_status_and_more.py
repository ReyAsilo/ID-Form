# Generated by Django 4.0.2 on 2022-02-09 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idrequestApp', '0002_facultytable_date_studenttable_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='facultytable',
            name='status',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='studenttable',
            name='status',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='studenttable',
            name='idpic',
            field=models.ImageField(blank=True, null=True, upload_to='img/%y'),
        ),
        migrations.AlterField(
            model_name='studenttable',
            name='signature',
            field=models.ImageField(blank=True, null=True, upload_to='img/&y '),
        ),
    ]
