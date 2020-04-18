# Generated by Django 2.1.1 on 2020-04-18 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0015_auto_20200418_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='link',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='listing',
            name='programcontact',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='listing',
            name='programdistribution',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='listing',
            name='programname',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='listing',
            name='programoriginator',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]