# Generated by Django 2.1.1 on 2020-04-17 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_auto_20200417_2301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='title',
            new_name='name',
        ),
    ]
