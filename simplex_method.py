import numpy as np


def simplex_method(tableau):

    # to hold the place of the variables
    n_variables = tableau.shape[0] + tableau.shape[1] - 2
    position = np.arange(1, n_variables+1, 1)

    condition = True

    while condition == True:

        # Find pivot column
        pivot_col = np.argmin(tableau[-1, :tableau.shape[0]])
        if tableau[-1, pivot_col] >= 0:
            condition = False
            break

        # Find pivot row
        ratios = tableau[0:-1, -1] / tableau[0:-1, pivot_col]
        for i in range(len(ratios)):
            if ratios[i] < 0:
                ratios[i] = np.inf
        pivot_row = np.argmin(ratios)

        # make new table
        new_tableau = np.copy(tableau)

        # to update the place of the variables
        temp1 = position[pivot_col]
        temp2 = position[(tableau.shape[1] - 1 + pivot_row)]
        position[pivot_col] = temp2
        position[(tableau.shape[1] - 1 + pivot_row)] = temp1


        for row in range(len(new_tableau)):
            if row == pivot_row:
                for column in range(len(new_tableau[row])):
                    if column == pivot_col:
                        new_tableau[pivot_row, pivot_col] = 1 / tableau[pivot_row, pivot_col]
                    else:
                        new_tableau[pivot_row, column] = tableau[pivot_row, column] / tableau[pivot_row, pivot_col]

            else:
                for column in range(len(new_tableau[row])):
                    if column == pivot_col:
                        new_tableau[row, pivot_col] = -tableau[row, pivot_col] / tableau[pivot_row, pivot_col]
                    else:
                        new_tableau[row, column] = tableau[row, column] + (
                                    (-tableau[row, pivot_col] / tableau[pivot_row, pivot_col]) * tableau[
                                pivot_row, column])

        tableau = new_tableau

    return tableau, position