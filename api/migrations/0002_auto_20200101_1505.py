# Generated by Django 3.0.1 on 2020-01-01 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductsTable',
            new_name='Product',
        ),
    ]
