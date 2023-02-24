# Generated by Django 4.1.3 on 2023-02-18 05:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('com_name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('com_winner', models.CharField(default='no winners', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Footballclub',
            fields=[
                ('fc_id', models.IntegerField(primary_key=True, serialize=False)),
                ('club_logo', models.CharField(max_length=240)),
                ('fc_name', models.CharField(max_length=255)),
                ('description', models.TextField(default='')),
                ('fc_email', models.EmailField(max_length=254)),
                ('fc_stadium', models.TextField(default='')),
                ('fc_location', models.TextField(default='')),
                ('position', models.IntegerField()),
                ('competing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='compi', to='club.competition')),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default='', max_length=254, verbose_name='email address')),
                ('firstname', models.CharField(default='', max_length=200)),
                ('lastname', models.CharField(default='', max_length=200)),
                ('manager_id', models.IntegerField(default='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Referee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default='', max_length=254, verbose_name='email address')),
                ('firstname', models.CharField(default='', max_length=200)),
                ('lastname', models.CharField(default='', max_length=200)),
                ('referee_id', models.IntegerField(default='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jersey', models.IntegerField()),
                ('managed_by', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='club.manager')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('match_timing', models.TextField(default='')),
                ('match_location', models.TextField(primary_key=True, serialize=False)),
                ('playedby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club.footballclub')),
                ('refereed_by', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='club.referee')),
            ],
        ),
        migrations.AddField(
            model_name='footballclub',
            name='managers',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='club.manager'),
        ),
    ]
