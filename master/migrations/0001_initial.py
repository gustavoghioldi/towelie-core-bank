from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('name', models.CharField(max_length=64)),
                ('iso_code', models.CharField(max_length=2, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('name', models.CharField(max_length=24, unique=True)),
                ('iso_code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('symbol', models.CharField(default='$', max_length=3)),
                ('decimal_places', models.SmallIntegerField(default=2)),
            ],
            options={
                'verbose_name_plural': 'Currencies',
            },
        ),
        migrations.CreateModel(
            name='Identifier',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('external_id', models.CharField(blank=True, max_length=128, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=128)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='master.country')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
