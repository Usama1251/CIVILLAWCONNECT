# Generated by Django 5.0.1 on 2024-04-20 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_profile_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default=(), max_length=100),
            preserve_default=False,
        ),
    ]