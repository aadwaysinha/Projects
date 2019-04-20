from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

app_name = 'voice'

urlpatterns = [
    url(r'^keyword/', views.keyword.as_view(), name='kwView'),
    url(r'^speechForm/', views.SpeechFormView, name='speachF'),
]
