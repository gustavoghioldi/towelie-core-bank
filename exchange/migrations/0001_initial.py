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
            name='HistoricalPrice',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('external_id', models.CharField(blank=True, max_length=128, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('source', models.CharField(max_length=64)),
                ('curreny', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='currency', to='master.currency')),
                ('reference_currency', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='reference_currency', to='master.currency')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
