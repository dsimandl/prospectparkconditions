# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conditions', '0002_reportlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='conditionreport',
            name='report_list',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
    ]
