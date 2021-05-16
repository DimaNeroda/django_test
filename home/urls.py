from django.contrib import admin
from django.urls import path

from home import views

urlpatterns = [
    path('', views.home_default, name='home_default'),

    path('ru/', views.home_ru, name='home_ru'),
    path('ua/', views.home_ua, name='home_ua'),
    path('en/', views.home_en, name='home_en'),

    # path('faculty/<int:id>/', views.faculty),
    path('faculty/', views.faculty),
    # path('course/<int:id>/', views.course),
    path('course/', views.course),
    # path('department/<int:id>/', views.department),
    path('department/', views.department),

    # path('charts/', views.charts),
    path('local_charts_teacher/', views.local_charts_teacher),
    path('local_charts_group/', views.local_charts_group),
    path('load_data', views.GetRequest.as_view())
]
