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
    moves.append(Move('a2','a3', movement.chessboard))
    
    moves.append(Move('a7','a5', movement.chessboard))
    
    moves.append(Move('b1','d3', movement.chessboard))
    
    # moves.append(Move('a2','a3', movement.chessboard))
    for move in moves:
        movement.move(move)

    data = {
        'range' : range(8),
        'chessboard' : chessboard.board,
        'errors' : chessboard.error.get_list_of_errors(),
        'test' : movement.whose_move(),
    }
    return render(request, 'chest_game/play_chest.html', data)