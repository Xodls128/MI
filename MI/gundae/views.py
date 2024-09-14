from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
#켈린더 이벤트 관리 모델
from .models import RecruitmentEvent
import numpy as np 
from sklearn.linear_model import LinearRegression
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

#계산기##
# 커트라인과 지원자 수 데이터 (과거 데이터)
past_cutoff_scores = np.array([84.0, 87.0, 91.0, 95.0, 97.0, 97.0, 95.0, 95.0, 95.0, 95.0]).reshape(-1, 1)
applicant_numbers = np.array([580, 1350, 1275, 986, 1148, 1298, 1090, 1032, 870, 573])

def general_technical_view(request):
    # 머신러닝 모델 (회귀 분석)
    model = LinearRegression()
    model.fit(applicant_numbers.reshape(-1, 1), past_cutoff_scores)

    # 지원자 수 예측을 위한 사용자 입력
    predicted_cutoff = model.predict([[573]])[0][0]  # 최근 지원자 수에 맞춰 예측

    # 기준 커트라인 점수
    last_cutoff_score = 95.0  # 가장 최근 커트라인

    if request.method == 'POST':
        # 사용자가 선택한 점수를 가져옵니다.
        license_score = int(request.POST.get('license_score', 0))
        attendance_score = int(request.POST.get('attendance_score', 0))
        interview_score = int(request.POST.get('interview_score', 0))
        
        # 가산점은 다중 선택이므로 getlist()로 처리
        additional_scores = request.POST.getlist('additional_score[]')  # 여러 개 선택 가능
        additional_score_total = sum([int(score) for score in additional_scores])  # 선택된 가산점 합계 계산

        print(f"추가 점수 리스트: {additional_scores}")
        print(f"추가 점수 합계: {additional_score_total}")

        # 총점 계산
        total_score = license_score + attendance_score + interview_score + additional_score_total
 
        # 합격 여부 판단 (예측된 커트라인 사용)
        if total_score >= predicted_cutoff:
            result = "합격이 예상됩니다. 잘 다녀오십시오 ^^7"
        else:
            result = "불합격이 예상됩니다.. 조금 더 부족한 부분을 채워봅시다."

        # 결과 페이지로 총점, 이전 커트라인, 예측 커트라인과 함께 전송
        return render(request, 'calculator/result.html', {
            'total': total_score, 
            'result': result, 
            'last_cutoff': last_cutoff_score, 
            'predicted_cutoff': predicted_cutoff
        })

    return render(request, 'calculator/general_technical.html')



# 커트라인 데이터 설정 (이전 데이터)
cutoff_data = {
    '전자계산': [77.0, 86.0, 88.0, 93.0, 96.0, 95.0, 85.0, 92.0],
    '화생방': [53.0, 66.0, 78.0, 74.0, 76.0, 76.0, 75.0, 74.0],
    '의무': [102.0, 88.0, 82.0, 91.0, 97.0, 105.0, 111.0, 113.0],
    '기계': [46.0, 46.0, 59.0, 67.0, 74.0, 71.0, 69.0, 62.0],
    '차량운전': [81.0, 84.0, 86.0, 88.0, 89.0, 91.0, 92.0, 90.0],
    '차량정비': [53.0, 52.0, 53.0, 54.0, 62.0, 70.0, 57.0, 55.0],
    '통신전자전기': [66.0, 67.0, 74.0, 79.0, 83.0, 72.0, 70.0, 67.0],
}

def special_technical_view(request):
    if request.method == 'POST':
        # 사용자가 선택한 직종
        job_category = request.POST.get('job_category')

        # 각 점수 가져오기
        license_score = int(request.POST.get('license_score', 0))
        major_score = int(request.POST.get('major_score', 0))
        attendance_score = int(request.POST.get('attendance_score', 0))
        interview_score = int(request.POST.get('interview_score', 0))
        additional_score = int(request.POST.get('additional_score', 0))

        # 총점 계산
        total_score = license_score + major_score + attendance_score + interview_score + additional_score

        # 선택한 직종에 대한 커트라인 점수 가져오기
        previous_cutoffs = np.array(cutoff_data.get(job_category, []))

        # 커트라인 데이터가 없으면 오류 처리
        if previous_cutoffs.size == 0:
            return render(request, 'calculator/result.html', {
                'total': total_score,
                'cutoff': '데이터 없음',
                'predicted_cutoff': '데이터 없음',
                'result': '데이터 부족으로 결과를 확인할 수 없습니다.',
                'job_category': job_category,
            })

        # 회귀 모델을 사용하여 예측된 커트라인 점수 계산
        model = LinearRegression()
        X = np.arange(len(previous_cutoffs)).reshape(-1, 1)
        y = previous_cutoffs
        model.fit(X, y)
        predicted_cutoff = model.predict([[len(previous_cutoffs)]])[0]  # 다음 시점에 대한 커트라인 예측

        # 선택한 직종의 이전 커트라인 점수 (가장 최근 값)
        previous_cutoff = previous_cutoffs[-1]

        # 합격 여부 판단
        if total_score >= predicted_cutoff:
            result = "합격"
        else:
            result = "불합격"

        # 결과 페이지로 전송
        return render(request, 'calculator/result.html', {
            'total': total_score,
            'cutoff': previous_cutoff,
            'predicted_cutoff': predicted_cutoff,
            'result': result,
            'job_category': job_category,
        })

    return render(request, 'calculator/special_technical.html')
