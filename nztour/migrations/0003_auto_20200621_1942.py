# Generated by Django 3.0.6 on 2020-06-21 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nztour', '0002_auto_20200621_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='days',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='destination',
            name='nights',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]