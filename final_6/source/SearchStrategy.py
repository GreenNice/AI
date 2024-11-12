import math

class SearchStrategy:
    @staticmethod
    def alpha_beta_search(problem):
        current_best_score = float('-inf')
        current_best_action = None
        alpha_cutoff = float('-inf')
        beta_cutoff = float('inf')
        depth = 3

        for action in problem.get_actions():
            problem.result(action, "O")
            score = SearchStrategy.abminimax(problem, alpha_cutoff, beta_cutoff, depth, False)
            problem.result(action, ' ')

            if score > current_best_score:
                current_best_score = score
                current_best_action = action

            alpha_cutoff = max(alpha_cutoff, current_best_score)
            if alpha_cutoff >= beta_cutoff:
                break

        return current_best_action

    @staticmethod
    def abminimax(problem, alpha, beta, depth, maximizing_player):
        if depth == 0 or problem.is_terminal():
            return problem.utility()

        if maximizing_player:
            value = float('-inf')
            for action in problem.get_actions():
                problem.result(action, "O")
                value = max(value, SearchStrategy.abminimax(problem, alpha, beta, depth - 1, False))
                problem.result(action, ' ')
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return value
        else:
            value = float('inf')
            for action in problem.get_actions():
                problem.result(action, "X")
                value = min(value, SearchStrategy.abminimax(problem, alpha, beta, depth - 1, True))
                problem.result(action, ' ')
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return value