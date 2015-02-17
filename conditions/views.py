from django.shortcuts import render, redirect
from conditions.models import ConditionReport

def home_page(request):
    return render(request, 'home.html')

def view_condition_report(request):
    reports = ConditionReport.objects.all()
    return render(request, 'condition_report.html', {'reports': reports})

def new_condition_report(request):
    ConditionReport.objects.create(date_time=request.POST['new_date_time'],
                                       road_condition=request.POST['new_road_condition'],
                                       weather_report=request.POST['new_weather_report'],
                                       crowds_report=request.POST['new_crowds_report'],
                                       report_notes=request.POST['new_report_notes'])
    return redirect('/condition-reports/the-only-report-in-the-world/')

