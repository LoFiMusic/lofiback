# Generated by Django 2.1 on 2018-09-09 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20180909_1621'),
    ]

    operations = [
        migrations.RenameField(
            model_name='music',
            old_name='author',
            new_name='artist',
        ),
        migrations.RenameField(
            model_name='music',
            old_name='cover',
            new_name='pic',
        ),
        migrations.RenameField(
            model_name='music',
            old_name='music_file',
            new_name='src',
        ),
        migrations.RenameField(
            model_name='music',
            old_name='name',
            new_name='title',
        ),
    ]
