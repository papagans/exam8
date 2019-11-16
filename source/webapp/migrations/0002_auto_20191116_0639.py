# Generated by Django 2.2 on 2019-11-16 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('other', 'Другое'), ('food', 'Еда'), ('clothes', 'Одежда'), ('household', 'Товары для дома')], max_length=50, verbose_name='Категория'),
        ),
    ]
