from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def onepage_scroll(request):
    # 각 섹션에 보여줄 데이터를 여기에 담을 수 있음
    sections = [
        {"title": "Section 1", "content": "This is the content for section 1"},
        {"title": "Section 2", "content": "This is the content for section 2"},
        {"title": "Section 3", "content": "This is the content for section 3"},
        {"title": "Section 4", "content": "This is the content for section 4"},
    ]
    return render(request, 'mainpage.html', {'sections': sections})


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

import json
from django.http import JsonResponse
from sklearn.linear_model import LinearRegression
import numpy as np

# 예시 커트라인 데이터 (예측 모델용)
applicant_numbers = np.array([500, 550, 600, 650, 700, 750])
past_cutoff_scores = np.array([90, 92, 94, 96, 98, 100])

def calculate_score(request):
    if request.method == 'POST':
        # POST 데이터를 JSON 형식으로 파싱
        data = json.loads(request.body)

        # 폼 데이터에서 점수 가져오기
        license_score = data.get('license_score', 0)
        attendance_score = data.get('attendance_score', 0)
        interview_score = data.get('interview_score', 0)
        additional_scores = data.get('additional_scores', [])
        
        # 가산점 합산
        additional_score_total = sum(additional_scores)

        # 총점 계산
        total_score = license_score + attendance_score + interview_score + additional_score_total

        # 머신러닝 모델 (회귀 분석) 설정
        model = LinearRegression()
        model.fit(applicant_numbers.reshape(-1, 1), past_cutoff_scores)

        # 예측된 커트라인 계산
        predicted_cutoff = model.predict([[573]])[0]  # 특정 지원자 수에 대한 예측 커트라인
        latest_cutoff = 95.0  # 가장 최근 커트라인 (예시)

        # 합격 여부 판단
        result = '합격 예상' if total_score >= predicted_cutoff else '불합격 예상'

        # 반환할 데이터 구성
        response_data = {
            'total_score': total_score,
            'result': result,
            'predicted_cutoff': predicted_cutoff,
            'latest_cutoff': latest_cutoff
        }

        return JsonResponse(response_data)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)
