# Generated by Django 4.0.6 on 2022-08-20 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_alter_client_country_nationality_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clientaddresses',
            options={'verbose_name_plural': 'Clients Addresses'},
        ),
        migrations.AlterModelOptions(
            name='clientids',
            options={'verbose_name_plural': 'Clients IDs'},
        ),
    ]