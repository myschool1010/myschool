# Generated by Django 3.1.5 on 2021-02-17 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_verify',
            field=models.BooleanField(default=False),
        ),
    ]