from django.shortcuts import render
from django.http import HttpResponse

def dashboard(request):
    data = {
        "title":  "Landing Page Dashboard",
    }
    return render(request, 'dashboard/index.html', data)
