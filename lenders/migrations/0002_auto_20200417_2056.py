# Generated by Django 2.1.1 on 2020-04-17 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lenders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lender',
            name='email',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='lender',
            name='location',
            field=models.TextField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='lender',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
