# Generated by Django 3.1.5 on 2021-04-06 04:41

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classroom', '0037_auto_20210404_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='date_of_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 6, 4, 41, 17, 642256, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='internshipform',
            name='end_date',
            field=models.DateField(blank=True, default=datetime.date(2021, 6, 5), help_text='yyyy-mm-dd', null=True),
        ),
        migrations.AlterField(
            model_name='internshipform',
            name='start_date',
            field=models.DateField(blank=True, default=datetime.date(2021, 4, 6), help_text='yyyy-mm-dd', null=True),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_json', models.TextField()),
                ('amount', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=255)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
