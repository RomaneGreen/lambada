# Generated by Django 2.1.1 on 2020-04-18 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0018_auto_20200418_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='city',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='listing',
            name='programtype',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
