# Generated by Django 3.1.5 on 2021-03-05 17:05

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]
    atomic = False

    operations = [
        migrations.RenameModel(
            old_name='Author',
            new_name='PostAuthor',
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 5, 17, 5, 24, 71473, tzinfo=utc)),
        ),
    ]
