# Generated by Django 3.0.8 on 2020-07-06 15:59

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('city', models.CharField(max_length=255, verbose_name='City')),
                ('country', models.CharField(max_length=255, verbose_name='Country')),
                ('ip', models.CharField(max_length=15, verbose_name='IP')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user', models.Model),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('image', models.TextField()),
                ('url_code', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='portfolio.Account')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255, verbose_name='City')),
                ('country', models.CharField(max_length=255, verbose_name='Country')),
                ('ip', models.CharField(max_length=15, verbose_name='IP')),
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
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Album')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Account')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Account')),
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
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Track')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TrackRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveSmallIntegerField(choices=[(1, 'POSITIVE'), (0, 'NEGATIVE')], verbose_name='Type of rating (1 - POSITIVE, 0 - NEGATIVE)')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Track')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Account')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GuestComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Guest')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CommentRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveSmallIntegerField(choices=[(1, 'POSITIVE'), (0, 'NEGATIVE')], verbose_name='Type of rating (1 - POSITIVE, 0 - NEGATIVE)')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.UserComment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Account')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AlbumRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveSmallIntegerField(choices=[(1, 'POSITIVE'), (0, 'NEGATIVE')], verbose_name='Type of rating (1 - POSITIVE, 0 - NEGATIVE)')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Album')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Account')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
