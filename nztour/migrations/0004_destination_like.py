# Generated by Django 3.0.6 on 2020-06-25 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nztour', '0003_auto_20200621_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='like',
            field=models.BooleanField(default=False),
        ),
    ]