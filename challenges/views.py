from django.http import HttpResponse, HttpResponseNotFound
import datetime


def index(request):
    return HttpResponse(
        "Bem-vindo ao calendário de desafios! Acesse /mes para ver o desafio do mês."
    )


def janeiro(request):
    return HttpResponse(
        "Janeiro - Desafio: Ler pelo menos 1 capítulo de um livro por dia."
    )


def fevereiro(request):
    return HttpResponse(
        "Fevereiro - Desafio: Fazer uma caminhada de pelo menos 20 minutos por dia."
    )


def marco(request):
    return HttpResponse(
        "Março - Desafio: Aprender algo novo durante 15 minutos por dia."
    )


def abril(request):
    return HttpResponse(
        "Abril - Desafio: Beber pelo menos 2 litros de água por dia."
    )


def maio(request):
    return HttpResponse(
        "Maio - Desafio: Organizar um espaço da casa por pelo menos 10 minutos por dia."
    )


def junho(request):
    return HttpResponse(
        "Junho - Desafio: Escrever em um diário pelo menos 3 vezes por semana."
    )


def julho(request):
    return HttpResponse(
        "Julho - Desafio: Passar pelo menos 30 minutos por dia sem usar redes sociais."
    )


def agosto(request):
    return HttpResponse(
        "Agosto - Desafio: Fazer pelo menos 20 minutos de atividade física por dia."
    )


def setembro(request):
    return HttpResponse(
        "Setembro - Desafio: Ler 10 páginas de um livro por dia."
    )


def outubro(request):
    return HttpResponse(
        "Outubro - Desafio: Fazer uma atividade criativa durante pelo menos 20 minutos por dia."
    )


def novembro(request):
    return HttpResponse(
        "Novembro - Desafio: Agradecer por uma coisa boa que aconteceu no dia."
    )


def dezembro(request):
    return HttpResponse(
        "Dezembro - Desafio: Fazer uma boa ação por dia."
    )


from django.http import HttpResponse, HttpResponseNotFound
import datetime


def monthly_challenges(request, month):
    """
    Mostra o desafio correspondente ao mês informado.
    """

    if month == 1:
        desafio = "Ler pelo menos 1 capítulo de um livro por dia."
        nome_mes = "Janeiro"

    elif month == 2:
        desafio = "Fazer uma caminhada de pelo menos 20 minutos por dia."
        nome_mes = "Fevereiro"

    elif month == 3:
        desafio = "Aprender algo novo durante 15 minutos por dia."
        nome_mes = "Março"

    elif month == 4:
        desafio = "Beber pelo menos 2 litros de água por dia."
        nome_mes = "Abril"

    elif month == 5:
        desafio = "Organizar um espaço da casa por pelo menos 10 minutos por dia."
        nome_mes = "Maio"

    elif month == 6:
        desafio = "Escrever em um diário pelo menos 3 vezes por semana."
        nome_mes = "Junho"

    elif month == 7:
        desafio = "Passar pelo menos 30 minutos por dia sem usar redes sociais."
        nome_mes = "Julho"

    elif month == 8:
        desafio = "Fazer pelo menos 20 minutos de atividade física por dia."
        nome_mes = "Agosto"

    elif month == 9:
        desafio = "Ler 10 páginas de um livro por dia."
        nome_mes = "Setembro"

    elif month == 10:
        desafio = "Fazer uma atividade criativa durante pelo menos 20 minutos por dia."
        nome_mes = "Outubro"

    elif month == 11:
        desafio = "Agradecer por uma coisa boa que aconteceu no dia."
        nome_mes = "Novembro"

    elif month == 12:
        desafio = "Fazer uma boa ação por dia."
        nome_mes = "Dezembro"

    else:
        return HttpResponseNotFound("Mês inválido. Informe um mês entre 1 e 12.")

    return HttpResponse(
        f"{nome_mes} - Desafio do mês: {desafio}"
    )

