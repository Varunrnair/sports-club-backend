# Generated by Django 4.1.3 on 2023-02-18 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0012_alter_player_managed_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='managed_by',
            new_name='coach',
        ),
    ]
