from copy import deepcopy

from .board import Board, CellState
from .player import Player, PLAYER_NAMES
import time 

class Game(object):
    
    win_x = 0
    win_o = 0
    draw = 0
    x_move_time = []
    o_move_time = []
    #copy of board declared
    board_copy = None
    #simulated board declared
    simulated_board = None
    #status of game
    board_size = 0
    def __init__(self, player_x, player_o, size=3, num_to_win=None,
                 starting_board=None):
        self._player_x = player_x
        self._player_o = player_o

        self._current_player = (Player.X, self._player_x)
        self._next_player = (Player.O, self._player_o)
        Game.board_size = int (input("How large would you like the board?"))
        win_num = int (input("How many to win?"))
        while win_num > Game.board_size:
            win_num =int (input(
                "The number to win cannot be larger than the board size.  Please enter a number less than the board size"))
        if starting_board is None:
            self._board = Board(size=Game.board_size, num_to_win=win_num)
            #copy of board initialized
            Game.board_copy = deepcopy(self._board)
            
        self._num_rounds = 0

    
    def play(self):
        #end value is set to none during the beginning of play
        Game.end_value = None
        while (self._board.winner is None
               and self._num_rounds < self._board.size ** 2):
            self._show_board()
            self._make_next_move()
            self._current_player, self._next_player = \
                self._next_player, self._current_player
            self._num_rounds = self._num_rounds + 1

        self._show_board()

        if self._board.winner is None:
            print("It's a draw!")
            Game.draw += 1
            self.set_value(0)
        else:
            print("Congratulations, {} won!".format(
                PLAYER_NAMES[self._board.winner]))
            if self._board.winner == 0:
                Game.win_x += 1
                self.set_value(1)
            else:
                Game.win_o += 1
                self.set_value(-1)
            
        print ("x wins: ", Game.win_x)
        print ("o wins: ", Game.win_o)
        print ("draw: ", Game.draw)

    def _show_board(self):
        print(self._board)
        print("")

    #return status of board   
    def get_board_copy(self):
        print (self._board)
        return self._board
        #return Game.board_copy

    def set_value(self, set_value):
        Game.end_value = set_value
    
    def _make_next_move(self):
        start_time = time.time()
        print("self. current player [1] ", self._current_player[0])
        move = self._current_player[1].next_move(deepcopy(self._board))
        print ("this is the move that's returned: ", move)
        move_time = time.time() - start_time
        if move.player == 0:
            Game.x_move_time.append(move_time)
        else: 
            Game.o_move_time.append(move_time)
        print ("move.player ", move.player)
        print ("self._current_player[0] ", self._current_player[0])
        assert move.player == self._current_player[0]
        assert self._board.cell(move.row, move.col) == CellState.EMPTY

        self._board.set_cell(move.player, move.row, move.col)
        Game.board_copy = deepcopy(self._board)
        

    