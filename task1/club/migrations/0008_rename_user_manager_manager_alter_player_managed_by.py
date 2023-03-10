# Generated by Django 4.1.3 on 2023-02-18 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0007_remove_manager_manager_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manager',
            old_name='user',
            new_name='manager',
        ),
        migrations.AlterField(
            model_name='player',
            name='managed_by',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='coach', to='club.manager'),
        ),
    ]
