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
    league_letter = 1
    #goal_list = Player.objects.order_by('g')
    goal_list = Player.objects.raw('SELECT * FROM player_player AS p JOIN team_team AS t ON p.team_id=t.id WHERE t.id=%s', [league_letter])
    assist_list = Player.objects.order_by('a')

    context = {
        'goal_list': goal_list,
    }
    return render(request, 'league/index.html', context)