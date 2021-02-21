from tic_tac_toe.game import Player, Game
from tic_tac_toe.agents.console_input_agent import ConsoleInputAgent
from tic_tac_toe.agents.random_agent import RandomAgent
from tic_tac_toe.agents.dfs_agent import DFS_Agent
from tic_tac_toe.agents.alpha_beta import Alpha_Beta
from tic_tac_toe.agents.my_agent import My_Agent
from tic_tac_toe.board import Board 
import numpy as np

AGENTS = [
    ("Human", ConsoleInputAgent), #ConsoleInputAgent
    ("Random_Agent", RandomAgent),
    ("DFS_Agent", DFS_Agent),
    ("Alpha_Beta", Alpha_Beta)
]

def _pick_agent(player):
    def _try_pick():
        try:
            list_of_agents = "\n".join(
                map(lambda x: "\t{} - {}".format(x[0], x[1][0]),
                    enumerate(AGENTS)))
            agent = int(
                input("Available agents: \n{}\nPick an agent [0-{}]: ".format(
                    list_of_agents, len(AGENTS) - 1)))
            return agent
        except ValueError:
            return None

    agent = _try_pick()

    while agent is None:
        print("Incorect selection, try again.")
        agent = _try_pick()
        
    return AGENTS[agent][1](player)


def main():
    print("Choosing player X...")
    player_x = _pick_agent(Player.X)

    print("Choosing player O...")
    player_o = _pick_agent(Player.O)
    play = "y"
    
    while play == "y":
        game = Game(player_x, player_o)
        game.play()
        print("check", Game.end_value)
        play = input("Play again? y/[n]: ")
    """
    count = 0
    while count < 10000:
        game = Game(player_x, player_o)
        game.play()
        count += 1
    """
    print ("Averge move time for x: ", x_average_move_time())
    print ("Averge move time for o: ", o_average_move_time())
    
def x_average_move_time():
    return np.average(np.array(Game.x_move_time))

def o_average_move_time():
    return np.average(np.array(Game.o_move_time))
        

        
if __name__ == "__main__":
    main()
