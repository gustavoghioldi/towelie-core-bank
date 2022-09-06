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
            name='Fund',
            fields=[
                ('balance', models.DecimalField(decimal_places=16, default=0.0, max_digits=48)),
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('external_id', models.CharField(blank=True, max_length=128, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=40)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='master.currency')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
