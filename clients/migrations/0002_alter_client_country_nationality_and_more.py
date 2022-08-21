# Generated by Django 4.0.6 on 2022-08-20 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='country_nationality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='country_nationality', to='master.country'),
        ),
        migrations.AlterField(
            model_name='client',
            name='country_residence',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='country_residence', to='master.country'),
        ),
    ]