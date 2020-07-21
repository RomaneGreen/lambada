# Generated by Django 2.1.1 on 2020-07-16 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0025_auto_20200527_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='blocks',
            field=models.TextField(blank=True, max_length=100, verbose_name='Countys Served'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='country',
            field=models.CharField(blank=True, max_length=100, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='eligible',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]
