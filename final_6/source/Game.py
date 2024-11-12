from Problem import Problem
from Board import Board
from SearchStrategy import SearchStrategy

class Game:
    def main():
        board = Board()
        problem = Problem(board)

        while not problem.is_terminal():
            board.draw()
            print("Your turn")
            row = int(input("Enter row number: "))
            col = int(input("Enter column number: "))
            if problem.board.is_valid_move(row, col):
                problem.result((row, col), 'X')
                if problem.is_terminal():
                    break
                computer_move = SearchStrategy.alpha_beta_search(problem)
                problem.result(computer_move, 'O')
            else:
                print("Invalid move. Try again.")
        board.draw()
        if problem.board.check_winner("O"):
            print("Computer wins!")
        elif problem.board.check_winner("X"):
            print("You win!")
        else:
            print("It's a draw!")

    if __name__ == "__main__":
        main()