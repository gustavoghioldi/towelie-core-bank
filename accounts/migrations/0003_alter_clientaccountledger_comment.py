# Generated by Django 4.0.6 on 2022-08-21 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_clientaccount_default_collector'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientaccountledger',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
