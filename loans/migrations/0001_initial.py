from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
        ('org', '0001_initial'),

    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('external_id', models.CharField(blank=True, max_length=128, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(blank=True, choices=[('SUBMITTED', 'Submitted'), ('APPROVED', 'Approved'), ('DISBURSED', 'Disbursed')], default='SUBMITTED', max_length=16, null=True)),
                ('principal', models.DecimalField(decimal_places=16, default=0.0, max_digits=48)),
                ('number_of_repayments', models.SmallIntegerField()),
                ('first_repayment_on', models.DateField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='clients.client')),
                ('loan_product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='org.loanproduct')),
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
            name='LoanLedger',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('external_id', models.CharField(blank=True, max_length=128, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('payment', models.SmallIntegerField()),
                ('payment_date', models.DateField()),
                ('payment_amount', models.DecimalField(decimal_places=16, default=0.0, max_digits=48)),
                ('amortization', models.DecimalField(decimal_places=16, default=0.0, max_digits=48)),
                ('interest', models.DecimalField(decimal_places=16, default=0.0, max_digits=48)),
                ('paid_out', models.BooleanField(default=False)),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='loans.loan')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='loan',
            name='loan_prupose',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='loans.loanpurpose'),
        ),
        migrations.AddField(
            model_name='loan',
            name='subimtted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Disbursed',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('external_id', models.CharField(blank=True, max_length=128, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('note', models.TextField()),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='loans.loan')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Approved',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('external_id', models.CharField(blank=True, max_length=128, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('note', models.TextField()),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='loans.loan')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
