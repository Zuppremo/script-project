from django.urls import path
from script.views import *

from . import views
app_name = 'script'

urlpatterns = [
    path('', views.index, name='index'),
    path('scripts/', views.ScriptListView.as_view(), name='script_list'),
    path('scripts/<int:pk>/', views.ScriptDetailView.as_view(), name='script_detail'),
    path('scripts/create/', views.ScriptCreateView.as_view(), name='script_create'),
    path('scripts/<int:pk>/edit/', views.ScriptUpdateView.as_view(), name='script_edit'),
    path('scripts/<int:pk>/delete/', views.ScriptDeleteView.as_view(), name='script_delete'),

    path('categories/', views.CategoryGroupListView.as_view(), name='category_list'),
    path('categories/create/', views.CategoryGroupCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/edit/', views.CategoryGroupUpdateView.as_view(), name='category_edit'),
    path('categories/<int:pk>/delete/', views.CategoryGroupDeleteView.as_view(), name='category_delete'),
    path('scripts/category/<int:pk>/', ScriptByCategoryListView.as_view(), name='script_by_category'),
]