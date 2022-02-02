

class Player:
    def __init__(self, symbol):
        self.symbol = symbol
        self.score = 0

    def play(self):
        row = col = None
        while True:
            try:
                row = int(input("Select Row: "))
                col = int(input("Select Column: "))
                if 0 <= row < 3 and 0 <= col < 3:
                    return row, col
                else:
                    print('Values out of range')
            except:
                print('Invalid value')


if __name__ == '__main__':
    a = Player('X')
    r, c = a.play()
    print(a.symbol, ' played at ', r, ' ', c)
