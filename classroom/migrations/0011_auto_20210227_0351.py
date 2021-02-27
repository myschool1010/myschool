# Generated by Django 3.1.5 on 2021-02-27 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0010_auto_20210221_1606'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseOverview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='CourseOverview', max_length=100, null=True)),
                ('text', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='course_overview',
            field=models.ManyToManyField(blank=True, to='classroom.CourseOverview'),
        ),
    ]