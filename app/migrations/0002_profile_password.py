# Generated by Django 5.0.1 on 2024-04-20 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='password',
            field=models.CharField(default=(), max_length=50),
            preserve_default=False,
        ),
    ]
