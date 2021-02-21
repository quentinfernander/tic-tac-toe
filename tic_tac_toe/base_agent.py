from abc import ABC, abstractmethod
from collections import namedtuple

from ..board import CellState
from ..player import PLAYER_NAMES


class Move(namedtuple("Move", ["player", "row", "col"])):
    def __repr__(self):
        return "Move(player={},row={},col={})".format(
            PLAYER_NAMES[self.player], self.row, self.col)


class Agent(ABC):
    def __init__(self, player):
        self._player = player

    @abstractmethod
    def next_move(self, board):    
        pass

    #player parameter added
    def _valid_moves(self, board): #added player parameter
        valid_moves = []
        for i, j in board.empty_cells:
            valid_moves.append(Move(self._player, i, j)) #used to be self._player

        return valid_moves
