# Generated by Django 2.2 on 2021-01-07 14:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=12)),
                ('image', models.ImageField(blank=True, default='no-profile-picture.jpg', null=True, upload_to='profile/')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descripción')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='Profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfiles',
            },
        ),
    ]
