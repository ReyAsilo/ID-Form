# Generated by Django 4.0.3 on 2022-05-27 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idrequestApp', '0003_alter_studenttable_idpic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studenttable',
            name='idpic',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='studenttable',
            name='signature',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]