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
    m1 = Move('e2','e4', movement.get_chessboard())
    movement.move(m1)
    m2 = Move('a7','a5', movement.get_chessboard())
    movement.move(m2)
    m3 = Move('h2','h4', movement.get_chessboard())
    movement.move(m3)
    m4 = Move('a8','a6', movement.get_chessboard())
    movement.move(m4)
    m5 = Move('b2','b3', movement.get_chessboard())
    movement.move(m5)
    
    m6 = Move('a6','e6', movement.get_chessboard())
    movement.move(m6)
    
    m7 = Move('e4','e5', movement.get_chessboard())
    movement.move(m7)
    m8 = Move('e6','e5', movement.get_chessboard())
    movement.move(m8)
    # m9 = Move('f1','d3', movement.get_chessboard())
    # movement.move(m9)
    m10 = Move('e1','f1', movement.get_chessboard())
    movement.move(m10)
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