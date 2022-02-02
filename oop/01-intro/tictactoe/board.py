

class Board:
    def __init__(self):
        self.grid = None
        self.create_grid()

    def create_grid(self):
        self.grid = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

    def display(self):
        for row in range(3):
            for col in range(3):
                print(self.grid[row][col] + " ", end='')
            print()

    def play(self, row, col, player):
        if self.grid[row][col] == '-':
            self.grid[row][col] = player
            return True
        else:
            return False

    def winner(self):
        # return the symbol of the winner, if any otherwise None
        return None

    def tie(self):
        # return true if Tie, false otherwise
        return False



if __name__ == '__main__':
    board = Board()
    board.play(1, 1, 'X')
    board.play(0, 1, 'O')
    board.display()


