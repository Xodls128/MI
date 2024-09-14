from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
#켈린더 이벤트 관리 모델
from .models import RecruitmentEvent
# Create your views here.
# 메인홈페이지
def home(request):
    return render(request, 'gundae/main.html')

# 켈린더 이벤트
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

