class Board:
    def __init__(self, size=8):
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]

    def draw(self):
        print("  ", end="")
        for i in range(self.size):
            print(f"  {i} ", end="")
        print()

        # Print horizontal divider
        print("  ", end="")
        for _ in range(self.size):
            print("+---", end="")
        print("+")

        for i, row in enumerate(self.board):
            print(f"{i} ", end="|")
            for cell in row:
                print(f" {cell} |", end="")
            print()

            print("  ", end="")
            for _ in range(self.size):
                print("+---", end="")
            print("+")


    def make_move(self, row, col, player):
        self.board[row][col] = player

    def is_valid_move(self, row, col):
        return 0 <= row < self.size and 0 <= col < self.size and self.board[row][col] == ' '

    def check_winner(self, player):
        for row in range(self.size):
            for col in range(self.size):
                if self.check_win_direction(player, row, col):
                    return True
        return False

    def check_win_direction(self, player, row, col):
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for dr, dc in directions:
            count = 0
            r, c = row, col
            while 0 <= r < self.size and 0 <= c < self.size and self.board[r][c] == player:
                count += 1
                r += dr
                c += dc
            r, c = row - dr, col - dc
            while 0 <= r < self.size and 0 <= c < self.size and self.board[r][c] == player:
                count += 1
                r -= dr
                c -= dc
            if count >= 4:
                return True
        return False

    def is_full(self):
        return all(cell != ' ' for row in self.board for cell in row)