# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conditions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportList',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
