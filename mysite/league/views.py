from django.shortcuts import render
from django.http import HttpResponse
from league.models import Team

from IPython import embed

# Create your views here.

def team(request,team_id):
    team = Team.objects.get(id=team_id)
    
    context={"team": team}
    
    response = render(request,'league/team_detail.html', context )
  
    return response

def team_list(request):
    
    team_list = Team.objects.all()        
    context={"team_list": team_list}
    response = render(request,'league/team_list.html', context )
    
    return response