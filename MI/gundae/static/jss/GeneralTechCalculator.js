//general_tech_calculator.js
//main.html의 body의 두번쨰 색션에 들어갈 계산기의 스크립트


ddocument.addEventListener('DOMContentLoaded', function() {
    const formContainer = document.getElementById('general_tech');

    const formHTML = `
        <div class="container mx-auto p-8 max-w-2xl">
            <!-- 카드 섹션 -->
            <div class="bg-white p-8 rounded-lg shadow-lg">
                <!-- 제목 -->
                <h1 class="text-3xl font-bold text-center text-blue-600 mb-6">공군 일반 기술병 점수 계산기</h1>
                <p class="text-center text-gray-600 mb-10">아래에서 골라 합격을 예측해보세요!</p>
                
                <!-- 폼 시작 -->
                <form method="POST" class="space-y-8">
                    <input type="hidden" name="csrfmiddlewaretoken" value="{{ csrf_token }}">
                    
                    <!-- 자격/면허 점수 (오름차순 정렬) -->
                    <div>
                        <label for="license_score" class="block text-lg font-semibold text-gray-700 mb-2">자격/면허 점수</label>
                        <p class="text-sm text-gray-500 mb-3">기술 자격증에 따라 점수가 다르게 부여됩니다. (최대 70점)</p>
                        <select class="block w-full p-3 border rounded-lg text-gray-700 focus:ring-2 focus:ring-blue-500" name="license_score" required>
                            <option value="0">자격증 없음 (0점)</option>
                            <option value="60">일반자격증 - L2 (60점)</option>
                            <option value="62">일반자격증 - L4, L3 (62점)</option>
                            <option value="64">일반자격증 - L6, L5 (64점)</option>
                            <option value="66">국가기술자격증 - 기능사 (66점)</option>
                            <option value="68">국가기술자격증 - 산업기사 (68점)</option>
                            <option value="70">국가기술자격증 - 기사 이상 (70점)</option>
                        </select>
                    </div>

                    <!-- 출결 점수 (오름차순 정렬) -->
                    <div>
                        <label for="attendance_score" class="block text-lg font-semibold text-gray-700 mb-2">출결 점수</label>
                        <p class="text-sm text-gray-500 mb-3">결석 일수에 따른 점수 (최대 20점)</p>
                        <select class="block w-full p-3 border rounded-lg text-gray-700 focus:ring-2 focus:ring-blue-500" name="attendance_score" required>
                            <option value="16">결석 7일 이상 (16점)</option>
                            <option value="17">결석 5~6일 (17점)</option>
                            <option value="18">결석 3~4일 (18점)</option>
                            <option value="19">결석 1~2일 (19점)</option>
                            <option value="20">결석 0일 (20점)</option>
                        </select>
                    </div>

                    <!-- 면접 점수 (오름차순 정렬) -->
                    <div>
                        <label for="interview_score" class="block text-lg font-semibold text-gray-700 mb-2">면접 점수</label>
                        <p class="text-sm text-gray-500 mb-3">면접 평가 결과에 따른 점수 (최대 35점)</p>
                        <select class="block w-full p-3 border rounded-lg text-gray-700 focus:ring-2 focus:ring-blue-500" name="interview_score" required>
                            <option value="25">면접 평가 부족 (25점)</option>
                            <option value="30">면접 평가 보통 (30점)</option>
                            <option value="35">면접 평가 우수 (35점)</option>
                        </select>
                    </div>

                    <!-- 가산점 (오름차순 정렬, 다중 선택 가능) -->
                    <div>
                        <label for="additional_score" class="block text-lg font-semibold text-gray-700 mb-2">가산점</label>
                        <p class="text-sm text-gray-500 mb-3">최대 15점, 여러 항목을 선택할 수 있습니다.</p>
                        <div class="grid grid-cols-1 gap-2">
                            <!-- 가산점 항목 (오름차순 정렬) -->
                            <div class="flex items-center">
                                <input type="checkbox" name="additional_score[]" value="1" id="option9" class="mr-2">
                                <label for="option9">병역진로설계 군 추천특기 (1점)</label>
                            </div>
                            <div class="flex items-center">
                                <input type="checkbox" name="additional_score[]" value="2" id="option6" class="mr-2">
                                <label for="option6">다자녀(2인) 가정자녀 (2점)</label>
                            </div>
                            <div class="flex items-center">
                                <input type="checkbox" name="additional_score[]" value="2" id="option10" class="mr-2">
                                <label for="option10">한국사능력검정 1, 2급 (2점)</label>
                            </div>
                            <div class="flex items-center">
                                <input type="checkbox" name="additional_score[]" value="4" id="option1" class="mr-2">
                                <label for="option1">국가 유공자 자녀/손자녀 (4점)</label>
                            </div>
                            <div class="flex items-center">
                                <input type="checkbox" name="additional_score[]" value="4" id="option2" class="mr-2">
                                <label for="option2">질병치유 자진입대 (4점)</label>
                            </div>
                            <div class="flex items-center">
                                <input type="checkbox" name="additional_score[]" value="4" id="option3" class="mr-2">
                                <label for="option3">현역병 입영대상으로 역종 변경 (4점)</label>
                            </div>
                        </div>
                    </div>

                    <!-- 계산하기 버튼 -->
                    <button type="submit" class="w-full bg-blue-500 hover:bg-blue-600 text-white py-3 rounded-lg font-semibold transition duration-300">점수 계산하기</button>

                    <!-- 초기화 버튼 -->
                    <button type="button" class="w-full bg-gray-500 hover:bg-gray-600 text-white py-3 rounded-lg font-semibold mt-4 transition duration-300" onclick="resetForm();">초기화</button>
                </form>
            </div>
        </div>
    `;

    formContainer.innerHTML = formHTML;

    // 폼 초기화 함수
    function resetForm() {
        document.querySelector('form').reset();
    }
});
