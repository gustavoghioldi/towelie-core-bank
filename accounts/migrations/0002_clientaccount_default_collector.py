# Generated by Django 4.0.6 on 2022-08-20 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientaccount',
            name='default_collector',
            field=models.BooleanField(default=False),
        ),
    ]