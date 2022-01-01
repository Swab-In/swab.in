# Generated by Django 3.2.8 on 2022-01-01 05:11

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
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=500)),
                ('foto', models.TextField()),
                ('author', models.CharField(max_length=140)),
                ('isi', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('komen', models.TextField()),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artikel.post')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
    ]
