# Generated by Django 4.0.6 on 2022-08-17 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_alter_clientids_unique_together'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ClientAccount',
        ),
    ]