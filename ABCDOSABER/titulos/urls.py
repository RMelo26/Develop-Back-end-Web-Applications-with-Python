from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('lista/', views.listar, name = 'listar' ),
    path('bomdia/', views.show_mensagem, name = 'bomdia'),
]

