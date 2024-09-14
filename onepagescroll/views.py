from django.shortcuts import render

from django.shortcuts import render

def onepage_scroll(request):
    # 각 섹션에 보여줄 데이터를 여기에 담을 수 있음
    sections = [
        {"title": "Section 1", "content": "This is the content for section 1"},
        {"title": "Section 2", "content": "This is the content for section 2"},
        {"title": "Section 3", "content": "This is the content for section 3"},
        {"title": "Section 4", "content": "This is the content for section 4"},
    ]
    return render(request, 'mainpage.html', {'sections': sections})

