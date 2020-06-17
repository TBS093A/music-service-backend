# Generated by Django 3.0.7 on 2020-06-17 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('song', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('song', models.ManyToManyField(to='song.Song')),
                ('user', models.ManyToManyField(to='account.Account')),
            ],
        ),
    ]
