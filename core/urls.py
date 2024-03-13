from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('aanmelden', views.aanmelden, name='aanmelden'),
    path('uitloggen', views.uitloggen, name='uitloggen'),
    path('hondAanmelden', views.hondAanmelden, name='hondAanmelden'),
    path('hondUitlaten', views.hondUitlaten, name='hondUitlaten'),
    path('honden', views.honden, name='honden'),
]
