# Generated by Django 2.1 on 2018-09-09 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180909_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='static_files/cover/'),
        ),
        migrations.AlterField(
            model_name='music',
            name='music_file',
            field=models.FileField(blank=True, upload_to='static_files/music/'),
        ),
    ]