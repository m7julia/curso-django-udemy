from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
import datetime
from django.urls import reverse 

monthly_challenges = {
    "janeiro": "Desafio: Ler pelo menos 1 capítulo de um livro por dia.",
    "fevereiro": "Desafio: Fazer uma caminhada de pelo menos 20 minutos por dia.",
    "marco" : "Desafio: Aprender algo novo durante 15 minutos por dia.",
    "abril" : "Desafio: Beber pelo menos 2 litros de água por dia.",
    "maio" : "Desafio: Organizar um espaço da casa por pelo menos 10 minutos por dia.",
    "junho" : "Desafio: Escrever em um diário pelo menos 3 vezes por semana.",
    "julho" : "Desafio: Passar pelo menos 30 minutos por dia sem usar redes sociais.",
    "agosto" : "Desafio: Fazer pelo menos 20 minutos de atividade física por dia.",
    "setembro" : "Desafio: Ler 10 páginas de um livro por dia.",
    "outubro" : "Desafio: Fazer uma atividade criativa durante pelo menos 20 minutos por dia.",
    "novembro" : "Desafio: Agradecer por uma coisa boa que aconteceu no dia.",
    "dezembro" : "Desafio: Fazer uma boa ação por dia."
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
        response_data  = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>Esse mês é invalido</h1>")