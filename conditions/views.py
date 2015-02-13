from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html', {
        'new_date_time_text': request.POST.get('new_date_time', ''),
        'new_road_condition_text': request.POST.get('new_road_condition', ''),
        'new_weather_report_text': request.POST.get('new_weather_report', ''),
        'new_crowds_report_text': request.POST.get('new_crowds_report', ''),
        'new_report_notes_text': request.POST.get('new_report_notes', ''),
    })


