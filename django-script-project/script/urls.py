from django.urls import path

from . import views

app_name = 'script'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:category_id>/', views.details, name='detail'),
]