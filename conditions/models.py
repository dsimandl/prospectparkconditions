from django.db import models

class ConditionReport(models.Model):
    date_time = models.TextField(default='')
    road_condition = models.TextField(default='')
    weather_report = models.TextField(default='')
    crowds_report = models.TextField(default='')
    report_notes = models.TextField(default='')

