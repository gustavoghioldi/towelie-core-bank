from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('master', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('external_id', models.CharField(blank=True, max_length=128, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('activation_date', models.DateField(blank=True, null=True)),
                ('country_nationality', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='country_nationality', to='master.country')),
                ('country_residence', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='country_residence', to='master.country')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClientMeta',
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
            name='Signup',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('external_id', models.CharField(blank=True, max_length=128, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('expires_at', models.DateTimeField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClientEAV',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('external_id', models.CharField(blank=True, max_length=128, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('attribute', models.CharField(max_length=25)),
                ('value', models.CharField(max_length=124)),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.client')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClientAddresses',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('external_id', models.CharField(blank=True, max_length=128, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(max_length=16)),
                ('description', models.TextField()),
                ('state', models.CharField(max_length=16)),
                ('country', models.CharField(max_length=3)),
                ('primary', models.BooleanField(default=False)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.client')),
            ],
            options={
                'verbose_name_plural': 'Clients Addresses',
            },
        ),
        migrations.CreateModel(
            name='ClientIds',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('external_id', models.CharField(blank=True, max_length=128, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(max_length=16)),
                ('id', models.CharField(max_length=32)),
                ('country', models.CharField(max_length=3)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.client')),
            ],
            options={
                'verbose_name_plural': 'Clients IDs',
                'unique_together': {('client', 'type', 'country')},
            },
        ),
    ]
