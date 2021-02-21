import random

from .base_agent import Agent
from tic_tac_toe.game import Game 
from tic_tac_toe.board import Board, CellState
from tic_tac_toe.player import Player, other_player
from copy import deepcopy



class DFS_Agent(Agent):
    def __init__(self, player):
        super().__init__(player)
        self.n_to_win = 0
    
    def get_branches(self, board, player, n):
        branches = []
        #print ("board copy", board)
        #if moves available
        if len(self._valid_moves(board)) != 0:
            for row in range(n):
                for column in range(n):
                    #if space on board is open
                    if board.cell(row, column) == -1:
                        #create copy of board
                        board_copy = deepcopy(board)
                        #make move on board copy and add board copy to branch list
                        branches.append(board_copy.set_cell(player, row, column))
        return branches

    def minimax(self, board, player, n):
        #winning condition
        if board.winner is not None: 
            
            if board.winner == 0:
                return 1
            else:
                return -1
        #draw condition
        if len(self._valid_moves(board)) == 0:
            return 0

        #game coninue condition
        utilities= []
        for branch in self.get_branches(board, player, n):
            utilities.append(self.minimax(branch, other_player(player),Game.board_size))
        if player == 0:
            #print ("max utility " , max(utilities))
            return max(utilities)
        else:
            #print ("min utility " , min(utilities))
            return min(utilities)
 
    def next_move(self, board):
        maximum = -2
        minimum = 2
        best_move = None
        for move in self._valid_moves(board):
            board_copy = deepcopy(board)
            board_copy.set_cell(move.player, move.row, move.col)
            utility = self.minimax(board_copy, other_player(self._player), Game.board_size)
            if self._player == 0:
                if utility > maximum:
                    maximum = utility
                    best_move = move
            else:
                if utility < minimum:
                    minimum = utility
                    best_move = move
        return best_move
    
    
        