import pickle
import copy
from django.shortcuts import render, redirect
from django.http import HttpResponse
from chest_game.logic.chessmans.pawn import Pawn
from chest_game.logic.chessboard import Chessboard
from chest_game.logic.movement import Movement
from chest_game.logic.move import Move
from chest_game.logic.game import Game
import random
from account.session_management import session_data
from account.session_management import session_edit
from account.session_management import session_game
from .forms import StartGameForm
from django.contrib.auth.decorators import login_required


def random_coor():
    return random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']) + random.choice(['1', '2', '3', '4', '5', '6', '7', '8'])

def main(request):
    return render(request, 'base/main.html')

def start_game(request):
    form = StartGameForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        opponent = form.cleaned_data.get('opponent')
        game = Game(session_data.get_user_if_logged(request.user.id), session_data.get_user_if_logged(opponent))
        return redirect('chest-game')
    
    form = StartGameForm()
    return render(request, 'game/start_game.html', {'form': form})

def move(request):
    game_name = request.session['game']
    game = session_game.get_game(game_name)
    game.move(request.POST.get("from", ""), request.POST.get("to", ""), session_data.get_user_if_logged(request.user.id))
    session_game.save_game(game)
    return redirect('chest-game')

def home(request):
    return render(request, 'base/main_login.html')

@login_required(login_url='/login/')
def game(request):
    # print(request.user)
    # chessboard = Chessboard()
    # movement = Movement(chessboard)
    # request.session['game'] = movement
    # moves = []
    # print(random_coor())
    # n = 0
    # while n < 10:
    #     while True:
    #         m1 = Move(random_coor(), random_coor(), movement.get_chessboard())
    #         movement.move(m1)
    #         if not chessboard.error.get_list_of_errors() or chessboard.error.get_list_of_errors() == 'win':
    #             break
    #     n += 1
    #     if chessboard.error.get_list_of_errors() == 'win':
    #         break

    # # m2 = Move('a7','a5', movement.get_chessboard())
    # # movement.move(m2)
    # # m3 = Move('f1','g2', movement.get_chessboard())
    # # movement.move(m3)
    # # m4 = Move('b7','b6', movement.get_chessboard())
    # # movement.move(m4)
    # # m5 = Move('g1','h3', movement.get_chessboard())
    # # movement.move(m5)
    
    # # m6 = Move('c8','b7', movement.get_chessboard())
    # # movement.move(m6)
    
    # # m7 = Move('e2','e4', movement.get_chessboard())
    # # movement.move(m7)
    # # m8 = Move('e7','e5', movement.get_chessboard())
    # # movement.move(m8)
    # # m9 = Move('e1','g1', movement.get_chessboard())
    # # movement.move(m9)
    # # m10 = Move('e1','g1', movement.get_chessboard())
    # # movement.move(m10)
    # # m11 = Move('e1','g1', movement.get_chessboard())
    # # movement.move(m11)
    # #moves.append(Move('a8','a7', movement.chessboard))
    # for movex in moves:
    #     movement.move(movex)
    if 'game' in request.session:
        # session_edit.clear_sessions()
        game_name = request.session['game']
        pickle_in = open('games/' + game_name, "rb")
        game = pickle.load(pickle_in)
        opponent_user = game.get_opponent_player(request.user)
        opponent_name = "AI poziom 1"
        if opponent_user is not None:
            opponent_name = opponent_user.username
        data = {
            'range' : range(8),
            'chessboard' :  game.movement.get_chessboard().board,
            'errors' : game.movement.chessboard.error.get_list_of_errors(),
            'test' : game.movement.whose_move(),
            'user' : session_data.get_user_if_logged(request.user.id),
            'game' : game_name,
            'x' : 'abcdefgh',
            'y' : '87654321',
            'users' : session_data.get_current_users(),
            'opponent' : opponent_name,
        }
    return render(request, 'game/play_chest.html', data)