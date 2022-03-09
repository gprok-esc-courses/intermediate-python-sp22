from windows.tictactoe_v2.player import Player


class Board:
    def __init__(self):
        self.grid = []
        self.reset()

    def play(self, player_value, row, col):
        if self.grid[row][col] == 0:
            self.grid[row][col] = player_value
            return True
        else:
            return False

    def winner(self):
        pass

    def is_tie(self):
        pass

    def reset(self):
        self.grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]