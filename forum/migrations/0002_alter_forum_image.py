# Generated by Django 3.2.8 on 2021-10-29 14:51
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='image',
            field=models.TextField(),
        ),
    ]