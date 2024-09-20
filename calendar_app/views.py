from django.http import JsonResponse
from .models import Event
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

def event_list(request):
    events = Event.objects.all()
    events_data = []
    
    for event in events:
        events_data.append({
            'title': event.title,
            'start': event.start_time.strftime('%Y-%m-%dT%H:%M:%S'),
            'end': event.end_time.strftime('%Y-%m-%dT%H:%M:%S') if event.end_time else None,
            'backgroundColor': event.backgroundColor,  # 색상 추가
            'announcement_date': event.announcement_date.strftime('%Y-%m-%d') if event.announcement_date else None,
            'applyUrl': event.applyUrl
        })
    return JsonResponse(events_data, safe=False)

@csrf_exempt
def add_event(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        announcement_date = request.POST.get('announcement_date', None)  # 합격발표일 추가

        # 문자열로 받은 날짜를 datetime 객체로 변환
        start_time = datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%S')
        end_time = datetime.strptime(end_time, '%Y-%m-%dT%H:%M:%S') if end_time else None
        announcement_date = datetime.strptime(announcement_date, '%Y-%m-%d') if announcement_date else None

        # 새 이벤트 저장
        event = Event.objects.create(
            title=title,
            start_time=start_time,
            end_time=end_time,
            announcement_date=announcement_date,  # 합격발표일 저장
        )
        return JsonResponse({'message': 'Event created successfully.'}, status=201)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def calendar_view(request):
    return render(request, 'calendar_app/calendar.html')
