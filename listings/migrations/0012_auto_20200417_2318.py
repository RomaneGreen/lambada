# Generated by Django 2.1.1 on 2020-04-17 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0011_auto_20200417_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='programoriginator',
            field=models.TextField(blank=True, max_length=30),
        ),
    ]