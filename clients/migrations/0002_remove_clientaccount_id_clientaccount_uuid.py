# Generated by Django 4.0.6 on 2022-07-16 17:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientaccount',
            name='id',
        ),
        migrations.AddField(
            model_name='clientaccount',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
