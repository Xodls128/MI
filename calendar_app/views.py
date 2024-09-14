from django.http import JsonResponse
from .models import RecruitmentEvent
from django.shortcuts import render


def event_data(request):
    events = RecruitmentEvent.objects.all()
    event_list = []
    for event in events:
        event_list.append({
            "title": f"{event.군별} - {event.모집분야}",
            "start": event.접수기간.split('~')[0] if event.접수기간 else None,  # 접수 시작일
            "end": event.접수기간.split('~')[1] if '~' in event.접수기간 else event.접수기간,  # 접수 종료일
        })
    return JsonResponse(event_list, safe=False)

def calendar_view(request):
    return render(request, 'calendar_app/calendar.html')
