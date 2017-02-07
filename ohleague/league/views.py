from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.views import generic
from league.models import League
from player.models import Player
from team.models import Team

# Create your views here.
def index(request):
    #E = 1, hmmm
    league_name = 'E'
    league_letter = 1
    #get players, filter by league_name, order by g (goals), need to add limit
    goal_list = Player.objects.raw('SELECT * FROM player_player AS p JOIN team_team AS t ON p.team_id=t.id JOIN league_league AS l ON t.league_id=l.id WHERE l.league_name=%s ORDER BY p.g DESC', [league_name])
    assist_list = Player.objects.raw('SELECT * FROM player_player AS p JOIN team_team AS t ON p.team_id=t.id WHERE t.id=%s ORDER BY p.a DESC', [league_letter])

    context = {
        'goal_list': goal_list,
        'assist_list': assist_list,
    }
    return render(request, 'league/index.html', context)