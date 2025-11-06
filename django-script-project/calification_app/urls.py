from django.urls import path

from . import views

app_name = 'calification_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('all_califications', views.all_califications, name='all_califications'),
    path('all_califications/', views.calificate, name='calificate'),
]