# Generated by Django 4.1.3 on 2023-02-18 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0009_remove_referee_email_remove_referee_firstname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='referee',
            old_name='user',
            new_name='referee',
        ),
    ]
