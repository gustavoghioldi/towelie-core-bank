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
            name='ClientAccount',
            fields=[
                ('balance', models.DecimalField(decimal_places=16, default=0.0, max_digits=48)),
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('external_id', models.CharField(blank=True, max_length=128, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('default_collector', models.BooleanField(default=False)),
                ('overdraw', models.DecimalField(decimal_places=16, default=0.0, max_digits=48)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='client_account_account', to='org.accountproduct')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='clients.client')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClientAccountLedger',
            fields=[
                ('balance', models.DecimalField(decimal_places=16, default=0.0, max_digits=48)),
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('external_id', models.CharField(blank=True, max_length=128, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('account_ledger_change_type', models.CharField(choices=[('DEBIT', 'Debit'), ('CREDIT', 'Credit')], max_length=128)),
                ('account_ledger_change_reason', models.CharField(max_length=24)),
                ('comment', models.TextField(blank=True, null=True)),
                ('client_account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.clientaccount')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
