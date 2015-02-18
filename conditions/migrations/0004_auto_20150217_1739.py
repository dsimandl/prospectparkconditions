# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conditions', '0003_conditionreport_report_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conditionreport',
            name='report_list',
            field=models.ForeignKey(default=None, to='conditions.ReportList'),
            preserve_default=True,
        ),
    ]
