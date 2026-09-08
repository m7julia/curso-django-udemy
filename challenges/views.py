from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
import datetime
from django.urls import reverse 
from django.shortcuts import render

monthly_challenges = {
    "janeiro": "Ler pelo menos 1 capítulo de um livro por dia.",
    "fevereiro": "Fazer uma caminhada de pelo menos 20 minutos por dia.",
    "marco" : "Aprender algo novo durante 15 minutos por dia.",
    "abril" : "Beber pelo menos 2 litros de água por dia.",
    "maio" : "Organizar um espaço da casa por pelo menos 10 minutos por dia.",
    "junho" : "Escrever em um diário pelo menos 3 vezes por semana.",
    "julho" : "Passar pelo menos 30 minutos por dia sem usar redes sociais.",
    "agosto" : "Fazer pelo menos 20 minutos de atividade física por dia.",
    "setembro" : "Ler 10 páginas de um livro por dia.",
    "outubro" : "Fazer uma atividade criativa durante pelo menos 20 minutos por dia.",
    "novembro" : "Agradecer por uma coisa boa que aconteceu no dia.",
    "dezembro" : "Fazer uma boa ação por dia."
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("monthly_challenge_str", args=[month]) 
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month >len(months):
        return HttpResponseNotFound("Mês inválido")

    redirec_month = months[month-1]
    redirec_path = reverse("monthly_challenge_str", args=[redirec_month]) 
    return HttpResponseRedirect(redirec_path)
    

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text
        })
    except:
        return HttpResponseNotFound("<h1>Esse mês é invalido</h1>")
    

