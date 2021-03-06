# Generated by Django 2.2 on 2019-11-04 08:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0004_auto_20191030_1846'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_me', models.TextField(blank=True, null=True, verbose_name='Обо мне')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='user_pics', verbose_name='Аватар')),
                ('github', models.URLField(blank=True, null=True, verbose_name='Github')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
        migrations.DeleteModel(
            name='UserGitHub',
        ),
    ]
