# Generated by Django 4.0.6 on 2022-08-24 15:41

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LoanRefiProduct',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('external_id', models.CharField(blank=True, max_length=128, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('opening_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='LoanProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('short_name', models.CharField(max_length=16)),
                ('description', models.TextField(blank=True, null=True)),
                ('start_date', models.DateField()),
                ('close_date', models.DateField()),
                ('amount_multiples', models.IntegerField()),
                ('principal_max', models.DecimalField(decimal_places=16, max_digits=48)),
                ('principal_min', models.DecimalField(decimal_places=16, max_digits=48)),
                ('repayments_max', models.SmallIntegerField()),
                ('repayments_min', models.SmallIntegerField()),
                ('repayment_step', models.SmallIntegerField()),
                ('amortization', models.CharField(choices=[('EQUALS_INSTALLMENTS', 'Equals Installments'), ('EQUAL_PRINCIPAL_PAYMENT', 'Equal Principal Payment')], max_length=64)),
                ('nominal_interes_rate', models.DecimalField(decimal_places=2, max_digits=6)),
                ('interes_method', models.CharField(choices=[('FLAT', 'Flat'), ('DECLINING_BALANCE', 'Declining Balance')], max_length=64)),
                ('interes_calculation_period', models.CharField(choices=[('DAILY', 'Daily'), ('SAME_AS_REPAYMENT_PERIOD', 'Same As Repayment Period')], max_length=64)),
                ('repaymenth_strategy', models.CharField(choices=[('PENALTIES_FEES_INTEREST_PRINCIPAL', 'Penalties Fees Interest Principal')], max_length=64)),
                ('interest_free_period', models.SmallIntegerField(default=0)),
                ('days_in_years', models.CharField(choices=[('360', ' 360'), ('364', ' 364'), ('365', ' 365')], max_length=8)),
                ('day_in_month', models.CharField(choices=[('30', ' 30'), ('ACTUAL', 'Actual')], max_length=8)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='master.country')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.currency')),
            ],
        ),
        migrations.CreateModel(
            name='AccountProduct',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('external_id', models.CharField(blank=True, max_length=128, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=24)),
                ('short_name', models.CharField(max_length=6)),
                ('default_overdraw', models.DecimalField(decimal_places=16, default=0.0, max_digits=48)),
                ('max_overdraw', models.DecimalField(decimal_places=16, default=0.0, max_digits=48)),
                ('collector', models.BooleanField(default=False)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='master.currency')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
