# Generated by Django 4.1.1 on 2022-10-14 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webshop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='characteristics',
        ),
    ]