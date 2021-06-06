from django.urls import path
from dorks import views

urlpatterns = [
    path('', views.dorks, name='advance_search'),
    path('google', views.google, name='google_search'),
    path('bing', views.bing, name='bing_search'),
    path('yandex', views.yandex, name='yandex_search'),
    path('shodan', views.shodan, name='shodan_search'),
    path('duckduckgo', views.duck, name='duck_search'),

]