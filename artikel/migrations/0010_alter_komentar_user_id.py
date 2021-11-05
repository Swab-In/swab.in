# Generated by Django 3.2.8 on 2021-11-05 05:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('artikel', '0009_alter_komentar_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='komentar',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
