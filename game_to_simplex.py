import numpy as np
import warnings


def game_to_simplex_table(payoff_matrix):

    min = np.amin(payoff_matrix)
    if min < 0:
        payoff_matrix = payoff_matrix + (min*-1)
        warnings.warn(f"the original payoff matrix has values below zero: corrected adding {min*-1} to the whole matrix)")

    #add column with ones
    new_column = np.ones(shape=(payoff_matrix.shape[0], 1))
    simplex_table = np.c_[payoff_matrix, new_column]

    #add row with -1 and last item 0
    new_row = np.full((1, simplex_table.shape[1] - 1), -1)
    new_row = np.c_[new_row, np.array([0])]
    simplex_table = np.r_[simplex_table, new_row]

    return simplex_table


def simplex_to_game_result(tableau, position):

    n_payoff_row = tableau.shape[0] - 1
    n_payoff_col = tableau.shape[1] - 1

    game_value = 1/tableau[-1, -1]
    prob_c = np.zeros((1, n_payoff_col))
    prob_r = np.zeros((1, n_payoff_row))

    n_variables = len(position)
    for i in range(n_variables):
        index = np.where(position == i + 1)[0][0]

        if i+1 <= n_payoff_col:
            if index >= n_payoff_col:
                value = tableau[index - n_payoff_col, -1]

            elif index < n_payoff_col:
                value = 0

            prob_c[0, i] = value

        elif i+1 > n_payoff_col:
            if index > n_payoff_col:
                value = 0

            elif index < n_payoff_col:
                value = tableau[-1, index]

            prob_r[0, i-n_payoff_col] = value

    prob_c = (prob_c*game_value)
    prob_r = (prob_r*game_value)

    return(game_value, prob_c, prob_r)
