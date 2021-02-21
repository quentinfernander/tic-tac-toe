import random

from .base_agent import Agent
from ..game import Game


class RandomAgent(Agent):
    def __init__(self, player):
        super().__init__(player)

    def next_move(self, board):
        return random.choice(Agent._valid_moves(self,board))

        