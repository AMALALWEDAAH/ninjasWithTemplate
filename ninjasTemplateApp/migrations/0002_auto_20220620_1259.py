# Generated by Django 2.2.4 on 2022-06-20 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ninjasTemplateApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dojos',
            name='city',
            field=models.CharField(max_length=64),
        ),
    ]
