from django.shortcuts import render

# Create your views here.
def gundaeapp_view(request):
    return render(request, 'gundaeapp/main.html')
