# Generated by Django 4.0 on 2021-12-27 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_link'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Link',
        ),
    ]