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

    from_coor1 = Coordinates('a8')
    to_coor1 = Coordinates('a3')
    movement.move(from_coor1, to_coor1)

    from_coor2 = Coordinates('b1')
    to_coor2 = Coordinates('c3')
    movement.move(from_coor2, to_coor2)

    from_coor3 = Coordinates('c8')
    to_coor3 = Coordinates('e6')
    movement.move(from_coor3, to_coor3)

    data = {
        'range' : range(8),
        'chessboard' : chessboard.board,
        'errors' : chessboard.error.get_list_of_errors(),
        'test' : movement.whose_move(),
    }
    return render(request, 'chest_game/play_chest.html', data)