# Generated by Django 2.1.1 on 2020-04-18 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0017_auto_20200418_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='city',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='listing',
            name='programtype',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='listing',
            name='zipcode',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]