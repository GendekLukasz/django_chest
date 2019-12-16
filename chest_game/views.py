import copy
from django.shortcuts import render
from django.http import HttpResponse
from chest_game.logic.chessmans.pawn import Pawn
from chest_game.logic.chessboard import Chessboard
from chest_game.logic.movement import Movement
from chest_game.logic.move import Move
import random

def random_coor():
    return random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']) + random.choice(['1', '2', '3', '4', '5', '6', '7', '8'])

def home(request):

    while True:
        chessboard = Chessboard()
        movement = Movement(chessboard)
        moves = []
        print(random_coor())
        n = 0
        while n < 30:
            while True:
                m1 = Move(random_coor(), random_coor(), movement.get_chessboard())
                movement.move(m1)
                if not chessboard.error.get_list_of_errors() or chessboard.error.get_list_of_errors() == 'win':
                    break
            n += 1
            if chessboard.error.get_list_of_errors() == 'win':
                break
        if chessboard.error.get_list_of_errors() == 'win':
            break
    # m2 = Move('a7','a5', movement.get_chessboard())
    # movement.move(m2)
    # m3 = Move('f1','g2', movement.get_chessboard())
    # movement.move(m3)
    # m4 = Move('b7','b6', movement.get_chessboard())
    # movement.move(m4)
    # m5 = Move('g1','h3', movement.get_chessboard())
    # movement.move(m5)
    
    # m6 = Move('c8','b7', movement.get_chessboard())
    # movement.move(m6)
    
    # m7 = Move('e2','e4', movement.get_chessboard())
    # movement.move(m7)
    # m8 = Move('e7','e5', movement.get_chessboard())
    # movement.move(m8)
    # m9 = Move('e1','g1', movement.get_chessboard())
    # movement.move(m9)
    # m10 = Move('e1','g1', movement.get_chessboard())
    # movement.move(m10)
    # m11 = Move('e1','g1', movement.get_chessboard())
    # movement.move(m11)
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