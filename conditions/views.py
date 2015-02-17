from django.shortcuts import render, redirect
from conditions.models import ConditionReport, ReportList

def home_page(request):
    return render(request, 'home.html')

def view_condition_report(request, report_list_id):
    report_list = ReportList.objects.get(id=report_list_id)
    return render(request, 'condition_report.html', {'report_list': report_list})

def new_condition_report(request):
    report_list = ReportList.objects.create()
    ConditionReport.objects.create(date_time=request.POST['new_date_time'],
                                       road_condition=request.POST['new_road_condition'],
                                       weather_report=request.POST['new_weather_report'],
                                       crowds_report=request.POST['new_crowds_report'],
                                       report_notes=request.POST['new_report_notes'],
                                       report_list=report_list)
    return redirect('/condition-reports/%d/' % (report_list.id,))

def add_condition_report(request, report_list_id):
    report_list = ReportList.objects.get(id=report_list_id)
    ConditionReport.objects.create(date_time=request.POST['new_date_time'],
                                       road_condition=request.POST['new_road_condition'],
                                       weather_report=request.POST['new_weather_report'],
                                       crowds_report=request.POST['new_crowds_report'],
                                       report_notes=request.POST['new_report_notes'],
                                       report_list=report_list)

    return redirect('/condition-reports/%d/' % (report_list.id,))


