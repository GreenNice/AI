class Problem:
    def __init__(self, board):
        self.board = board

    def get_actions(self):
        actions = []
        for row in range(self.board.size):
            for col in range(self.board.size):
                if self.board.is_valid_move(row, col):
                    actions.append((row, col))
        return actions

    def result(self, action, player):
        row, col = action
        self.board.make_move(row, col, player)

    def is_terminal(self):
        return self.board.check_winner("X") or self.board.check_winner("O") or self.board.is_full()

    def utility(self):
        if self.board.check_winner("O"):
            return 1
        elif self.board.check_winner("X"):
            return -1
        else:
            return 0

    