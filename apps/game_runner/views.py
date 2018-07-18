from django.shortcuts import render, HttpResponse, redirect
from django import template
from .classes.game import Game

register = template.Library()
@register.filter(name='get_class')
def get_class(value):
    return value.__class__.__name__


# Create your views here.
def start(request):
    if 'stable' not in request.session:
        redirect('/')
        
    players = []
    for player in range(1,request.session['player_count'] +1):
        players.append([request.session['p' + str(player) + '_name'], "human"])
    print(players)
    if 'single_player_flag' in request.session:
        print("its in session")
        players.append(['computer player 1', "computer"])
    context = {
        "players" : players,
    }
    request.session['players'] = players
    return render(request, "game_runner/start.html", context)

def go(request):
    if 'stable' not in request.session:
        redirect('/')

    game1 = Game(request.session['players'], "none")
    context = {
        "game" : game1
    }
    return render(request, "game_runner/game_board.html", context)