# Generated by Django 3.1.5 on 2021-02-03 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210203_0342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorites',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.user'),
        ),
    ]
