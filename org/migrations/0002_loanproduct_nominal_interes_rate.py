# Generated by Django 4.0.6 on 2022-07-16 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanproduct',
            name='nominal_interes_rate',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=6),
            preserve_default=False,
        ),
    ]
