from django.shortcuts import render
from django.http import HttpResponse
from chest_game.logic.chessmans.pawn import Pawn
from chest_game.logic.chessboard import Chessboard
from chest_game.logic.movement import Movement
from chest_game.logic.coordinates import Coordinates

def home(request):
    chessboard = Chessboard()
    movement = Movement(chessboard)
    from_coor = Coordinates('a2')
    to_coor = Coordinates('a3')
    movement.move(from_coor, to_coor)
    data = {
        'range' : range(8),
        'chessboard' : chessboard.board,
    }
    return render(request, 'chest_game/play_chest.html', data)