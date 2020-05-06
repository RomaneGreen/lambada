# Generated by Django 2.1.1 on 2020-05-06 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0023_auto_20200418_0122'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='listing',
            options={'verbose_name': 'Program', 'verbose_name_plural': 'Programs'},
        ),
        migrations.AlterField(
            model_name='listing',
            name='participatinglenders',
            field=models.CharField(blank=True, max_length=400, verbose_name='Participating Lender'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='programcontact',
            field=models.CharField(blank=True, max_length=400, verbose_name='Program Contact'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='programdistribution',
            field=models.CharField(blank=True, max_length=400, verbose_name='Program Distribution'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='programname',
            field=models.CharField(blank=True, max_length=400, verbose_name='Program Name'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='programoriginator',
            field=models.TextField(blank=True, max_length=400, verbose_name='Program Originator'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='programtype',
            field=models.CharField(blank=True, max_length=500, verbose_name='Program Type'),
        ),
    ]