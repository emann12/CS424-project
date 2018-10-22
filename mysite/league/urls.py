from django.urls import path
from . import views

urlpatterns = [
    path('team/id/<int:team_id>', views.team),
    path('team_list', views.team_list),
]