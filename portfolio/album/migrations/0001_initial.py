# Generated by Django 3.0.8 on 2020-07-24 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('image', models.TextField()),
                ('url_code', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account.Account')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=1000)),
                ('text', models.TextField()),
                ('image', models.TextField()),
                ('audio', models.TextField()),
                ('url_code', models.CharField(max_length=255)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='album.Album')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Account')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TrackRow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row_number', models.IntegerField()),
                ('group', models.BooleanField()),
                ('leader', models.BooleanField()),
                ('link', models.IntegerField(default=None)),
                ('text', models.TextField(default=None)),
                ('description', models.TextField(default=None)),
                ('image', models.TextField(default=None)),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='album.Track')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]