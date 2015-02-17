from django.db import models

class ReportList(models.Model):
    pass

class ConditionReport(models.Model):
    date_time = models.TextField(default='')
    road_condition = models.TextField(default='')
    weather_report = models.TextField(default='')
    crowds_report = models.TextField(default='')
    report_notes = models.TextField(default='')
    report_list = models.ForeignKey(ReportList, default=None)