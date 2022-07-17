# Generated by Django 4.0.6 on 2022-07-17 20:14

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoanApproved',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('external_id', models.CharField(blank=True, max_length=128, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('at', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LoanDisbursement',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('external_id', models.CharField(blank=True, max_length=128, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('at', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LoanPurpose',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('external_id', models.CharField(blank=True, max_length=128, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=25)),
                ('code', models.CharField(max_length=4)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LoanSubmitted',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('external_id', models.CharField(blank=True, max_length=128, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('at', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('principal', models.DecimalField(decimal_places=16, max_digits=48)),
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('external_id', models.CharField(blank=True, max_length=128, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('number_of_repayments', models.SmallIntegerField()),
                ('first_repayment_on', models.DateField()),
                ('approved', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='loans.loanapproved')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='clients.client')),
                ('disbursement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='loans.loandisbursement')),
                ('loan_prupose', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='loans.loanpurpose')),
                ('submitted', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='loans.loansubmitted')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
