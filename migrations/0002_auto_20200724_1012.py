# Generated by Django 3.0.8 on 2020-07-24 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CommentRating',
            new_name='GuestCommentRating',
        ),
        migrations.AlterField(
            model_name='guestcommentrating',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.GuestComment'),
        ),
        migrations.CreateModel(
            name='UserCommentRating',
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
    ]