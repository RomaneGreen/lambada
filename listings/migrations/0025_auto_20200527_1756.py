# Generated by Django 2.1.1 on 2020-05-27 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0024_auto_20200506_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='Neighborhoods',
            field=models.TextField(blank=True, verbose_name='Neighborhoods Served'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='ami',
            field=models.IntegerField(blank=True, null=True, verbose_name='Amount '),
        ),
        migrations.AlterField(
            model_name='listing',
            name='amount',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='AMI'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='country',
            field=models.CharField(blank=True, max_length=2, verbose_name='County'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='minimumcontribution',
            field=models.IntegerField(blank=True, null=True, verbose_name='Minimum Contribution'),
        ),
    ]
