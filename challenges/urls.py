from django.urls import path
from . import views

urlpatterns = [
    path("<int:month>", views.monthly_challenges, name="monthly_challenge_int"),
    path("<str:month>", views.monthly_challenges, name="monthly_challenge_str"),

    path("janeiro", views.janeiro, name="janeiro"),
    path("fevereiro", views.fevereiro, name="fevereiro"),
    path("marco", views.marco, name="marco"),
    path("abril", views.abril, name="abril"),
    path("maio", views.maio, name="maio"),
    path("junho", views.junho, name="junho"),
    path("julho", views.julho, name="julho"),
    path("agosto", views.agosto, name="agosto"),
    path("setembro", views.setembro, name="setembro"),
    path("outubro", views.outubro, name="outubro"),
    path("novembro", views.novembro, name="novembro"),
    path("dezembro", views.dezembro, name="dezembro"),
]