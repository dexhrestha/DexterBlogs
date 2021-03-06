# Generated by Django 2.0.6 on 2018-09-22 10:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_album_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='song_url',
            field=models.CharField(default='', max_length=512),
        ),
        migrations.AlterField(
            model_name='album',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
