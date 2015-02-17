from django.shortcuts import render, redirect
from conditions.models import ConditionReport

def home_page(request):
    if request.method == 'POST':
        ConditionReport.objects.create(date_time=request.POST['new_date_time'],
                                       road_condition=request.POST['new_road_condition'],
                                       weather_report=request.POST['new_weather_report'],
                                       crowds_report=request.POST['new_crowds_report'],
                                       report_notes=request.POST['new_report_notes'])
        return redirect('/conditionreports/the-only-report-in-the-world/')

    return render(request, 'home.html')

def view_conditionreport(request):
    reports = ConditionReport.objects.all()
    return render(request, 'conditionreport.html', {'reports': reports})

