# Generated by Django 2.2 on 2019-11-16 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20191104_0918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='github',
        ),
    ]
