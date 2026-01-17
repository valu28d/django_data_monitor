from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return HttpResponse("Hello, authenticated user!")
    
@login_required
def dashboard(request):

    response = requests.get(settings.API_URL)  # URL de la API
    posts = response.json()  # Convertir la respuesta a JSON

    # Número total de respuestas
    total_responses = len(posts)
    #usuarios unicos
    unique_users = len(set([p["userId"] for p in posts]))
    # numero de post por usuario
    posts_per_user = round(total_responses / unique_users, 2)
    # promedip de respuestas por usuario
    avg_responses_per_user = round(total_responses / unique_users, 2)
    # tabala de los primeros 10 titulos
    table_data = [{"valor1": p["id"], "valor2": p["title"]} for p in posts[:10]]


    data = {
        "title":  "Landing Page Dashboard",
        'total_responses': total_responses,
        "unique_users": unique_users,
        "posts_per_user": posts_per_user,
        "avg_responses_per_user": avg_responses_per_user,
        "table_data": table_data,
    }
    return render(request, 'dashboard/index.html', data)



