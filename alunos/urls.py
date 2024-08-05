from django.urls import path
from alunos.views import index, geraldo, alana

urlpatterns = [
    path('',index,name='index'),
    path('index/',index,name='index'),
    path('geraldo/',geraldo,name='geraldo'),
    path('alana/',alana,name='alana'),
]