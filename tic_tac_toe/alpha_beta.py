import random

from .base_agent import Agent
from tic_tac_toe.game import Game 
from tic_tac_toe.board import Board, CellState
from tic_tac_toe.player import Player, other_player
from copy import deepcopy



class Alpha_Beta(Agent):
    def __init__(self, player):
        super().__init__(player)
    
    def get_branches(self, board, player, n):
        branches = []
        # print ("player in get_branches ", player)
        #print ("board that's passed in ", board)
        if len(self._valid_moves(board)) != 0:
            for row in range(n):
                for column in range(n):
                    if board.cell(row, column) == -1:
                        board_copy = deepcopy(board)
                        branches.append(board_copy.set_cell(player, row, column))
                        #print ("board_copy ", board)
        return branches
    
    def max_val(self, board, player, alpha, beta):
        if board.winner is not None:
            if board.winner == 0:
                return 1
            else:
                return -1
        # if self._valid_moves(board) == 0:
        if len(self._valid_moves(board)) == 0:
                return 0
        value = -2
        for branch in self.get_branches(board, player, Game.board_size):
            min_evaluation = self.min_val(branch, other_player(player), alpha, beta)
            value = max(value, min_evaluation)
            alpha = max(alpha, min_evaluation)
            # print ("max val alpha ", alpha)
            # print ("max val beta ", beta)
            if alpha >= beta:
                break
        # you should return the maximum value, which could be lower than alpha
        # return alpha
        return value

    def min_val(self, board, player, alpha, beta):
        if board.winner is not None:
            if board.winner == 0:
                return 1
            else:
                return -1
        # if self._valid_moves(board) == 0:
        if len(self._valid_moves(board)) == 0:
                return 0
        # print ("player in min_val ", player)
        value = 2
        for branch in self.get_branches(board, player, Game.board_size):
            max_evaluation = self.max_val(branch, other_player(player), alpha, beta)
            value = min(value, max_evaluation)
            beta = min(beta, max_evaluation)
            # print ("min val alpha ", alpha)
            # print ("min val beta ", beta)
            if alpha >= beta:
                break
        # you should return the minimum value, which could be higher than beta
        # return beta
        return value

    def next_move(self, board):
        maximum = -2
        minimum = 2
        best_move = None
        # print("board ", board)
        valid_moves = self._valid_moves(board)
        random.shuffle(valid_moves)
        for move in valid_moves:
            board_copy = deepcopy(board)
            board_copy.set_cell(move.player, move.row, move.col)
            if self._player == 0:
                # other player is O, and therefore min
                # antoher way to look at it is, in this loop you're picking
                # the maximum value, so you should recurse by picking the
                # minimum
                # utility = self.max_val(board_copy, other_player(self._player), -2, 2)
                utility = self.min_val(board_copy, other_player(self._player), -2, 2)
                if utility > maximum:
                    maximum = utility
                    best_move = move
                    #print("best " ,best_move)
            else:
                # utility = self.min_val(board_copy, other_player(self._player), -2, 2)
                utility = self.max_val(board_copy, other_player(self._player), -2, 2)
                if utility < minimum:
                    minimum = utility
                    best_move = move
                    #print("best ", best_move)
        print ("Best move" , best_move)
        return best_move
         
    

    
    
    
