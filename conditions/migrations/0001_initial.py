# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConditionReport',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('date_time', models.TextField(default='')),
                ('road_condition', models.TextField(default='')),
                ('weather_report', models.TextField(default='')),
                ('crowds_report', models.TextField(default='')),
                ('report_notes', models.TextField(default='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
