// calender.js 
//main.html의 body의 첫번쨰 색션에 들어갈 켈린더의 스크립트


document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calender');
    // 랜더링 위치( id가 calender인 곳에 랜더링됨 )

    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        locale: 'ko',
        events: '/calendar/events/',  // Django에서 데이터를 가져올 URL
        headerToolbar: {
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth'
        },
        buttonText: {
            today: '오늘',
            month: '월',
            week: '주',
            day: '일'
        },
        eventClick: function(info) {
            var modalHtml = `
                <div class="modal fade" id="eventModal" tabindex="-1" aria-labelledby="eventModalLabel" aria-hidden="true">
                    <div class="modal-dialog">
                        <div class="modal-content">
                            <div class="modal-header">
                                <h5 class="modal-title" id="eventModalLabel">${info.event.title}</h5>
                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            </div>
                            <div class="modal-body">
                                <p><strong>시작일:</strong> ${info.event.start.toLocaleDateString()}</p>
                                <p><strong>종료일:</strong> ${info.event.end ? info.event.end.toLocaleDateString() : 'N/A'}</p>
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">닫기</button>
                            </div>
                        </div>
                    </div>
                </div>
            `;

            document.body.insertAdjacentHTML('beforeend', modalHtml);
            var eventModal = new bootstrap.Modal(document.getElementById('eventModal'));
            eventModal.show();

            document.getElementById('eventModal').addEventListener('hidden.bs.modal', function() {
                document.getElementById('eventModal').remove();
            });
        }
    });

    calendar.render();
});