# Generated by Django 4.1.3 on 2023-02-18 07:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('club', '0002_rename_user_player_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='managed_by',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='manager', to='club.manager'),
        ),
        migrations.AlterField(
            model_name='player',
            name='player',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='player', to=settings.AUTH_USER_MODEL),
        ),
    ]
