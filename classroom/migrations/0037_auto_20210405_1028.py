# Generated by Django 3.1.5 on 2021-04-05 10:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0036_auto_20210403_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='date_of_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 5, 10, 28, 45, 182277, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='internshipform',
            name='end_date',
            field=models.DateField(blank=True, default=datetime.date(2021, 6, 4), help_text='yyyy-mm-dd', null=True),
        ),
        migrations.AlterField(
            model_name='internshipform',
            name='start_date',
            field=models.DateField(blank=True, default=datetime.date(2021, 4, 5), help_text='yyyy-mm-dd', null=True),
        ),
    ]