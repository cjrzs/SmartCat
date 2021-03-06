# Generated by Django 2.2.16 on 2021-09-30 11:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main_server', '0004_auto_20210928_1326'),
    ]

    operations = [

        migrations.AlterField(
            model_name='content',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 30, 11, 9, 25, 337377, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='content',
            name='delete_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 30, 11, 9, 25, 337377, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 30, 11, 9, 25, 337377, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='media',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 30, 11, 9, 25, 337377, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='media',
            name='delete_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 30, 11, 9, 25, 337377, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 30, 11, 9, 25, 337377, tzinfo=utc)),
        ),
    ]
