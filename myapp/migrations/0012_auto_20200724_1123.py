# Generated by Django 2.2.5 on 2020-07-24 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_award'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='award',
            name='description',
        ),
        migrations.RemoveField(
            model_name='award',
            name='name',
        ),
    ]
