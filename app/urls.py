from django.contrib import admin
from django.urls import path, include
from .views import news_list, news_detail, home_page, uzb_page, jahon_page, sport_page, fan_page

urlpatterns = [
    path('', home_page, name='home'),
    path('uzbekiston/', uzb_page, name='uzb_page'),
    path('jahon/', jahon_page, name='jahon_page'),
    path('sport/', sport_page, name='sport_page'),
    path('fan/', fan_page, name='fan_page'),
    path("news/<int:id>", news_detail, name='news_detail_page'),
]
