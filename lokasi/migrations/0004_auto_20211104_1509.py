# Generated by Django 3.2.8 on 2021-11-04 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lokasi', '0003_post_lokasi_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='detail',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='lokasi',
        ),
    ]
