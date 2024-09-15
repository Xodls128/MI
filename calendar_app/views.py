from django.http import JsonResponse
from .models import Event
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def event_list(request):
    events = Event.objects.all()
    events_data = []
    
    for event in events:
        events_data.append({
            'title': event.title,
            'start': event.start_time.strftime('%Y-%m-%dT%H:%M:%S'),
            'end': event.end_time.strftime('%Y-%m-%dT%H:%M:%S') if event.end_time else None,
            'description': event.description,
            'color': event.color,  # 색상 추가
            'content': event.content,  # 추가적인 설명 추가
        })
    return JsonResponse(events_data, safe=False)

@csrf_exempt
def add_event(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        description = request.POST.get('description', '')
        
        # 새 이벤트 저장
        event = Event.objects.create(
            title=title,
            start_time=start_time,
            end_time=end_time,
            description=description,
        )
        return JsonResponse({'message': 'Event created successfully.'}, status=201)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def calendar_view(request):
    return render(request, 'calendar_app/calendar.html')
