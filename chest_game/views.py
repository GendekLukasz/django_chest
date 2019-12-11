import copy
from django.shortcuts import render
from django.http import HttpResponse
from chest_game.logic.chessmans.pawn import Pawn
from chest_game.logic.chessboard import Chessboard
from chest_game.logic.movement import Movement
from chest_game.logic.move import Move

def home(request):
    chessboard = Chessboard()
    movement = Movement(chessboard)
    moves = []
    m1 = Move('b1','a3', movement.get_chessboard())
    movement.move(m1)
    m2 = Move('e7','e5', movement.get_chessboard())
    movement.move(m2)
    m3 = Move('h2','h4', movement.get_chessboard())
    movement.move(m3)
    m4 = Move('f8','b4', movement.get_chessboard())
    movement.move(m4)
    m5 = Move('d2','d3', movement.get_chessboard())
    movement.move(m5)
    
    # m6 = Move('e7','e5', movement.get_chessboard())
    # movement.move(m6)
    
    # m6 = Move('d1','b3', movement.get_chessboard())
    # movement.move(m6)
    #moves.append(Move('a8','a7', movement.chessboard))
    for movex in moves:
        movement.move(movex)

    data = {
        'range' : range(8),
        'chessboard' :  movement.get_chessboard().board,
        'errors' : chessboard.error.get_list_of_errors(),
        'test' : movement.whose_move(),
    }
    return render(request, 'chest_game/play_chest.html', data)