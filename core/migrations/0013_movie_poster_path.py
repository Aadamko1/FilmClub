# Generated by Django 3.1.5 on 2021-02-13 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20210213_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='poster_path',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
