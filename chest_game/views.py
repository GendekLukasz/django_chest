from django.shortcuts import render
from django.http import HttpResponse
from chest_game.logic.chessmans.pawn import Pawn
from chest_game.logic.chessboard import Chessboard
from chest_game.logic.movement import Movement

def home(request):
    chessboard = Chessboard()
    movement = Movement(chessboard)
    movement.move([1,0],[7,0])
    data = {
        'range' : range(8),
        'chessboard' : chessboard.board,
    }
    return render(request, 'chest_game/play_chest.html', data)