# Generated by Django 2.2 on 2020-07-26 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20200725_1231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='award',
            name='award_number',
        ),
        migrations.AlterField(
            model_name='about',
            name='contact',
            field=models.CharField(max_length=50),
        ),
    ]