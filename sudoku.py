import argparse             # For Parsing Arguments
import logging              # For Debugging Functions
import timeit               # Timing

def solve_sudoku(assignment):
    # If there is no unassigned location, there are three possibilities:
    # 1. We solved the puzzle
    # 2. The puzzle given to us is already filled and is solved
    # 3. The puzzle given to us is already filled but is wrong. This is
    #    already ruled out in the conditional in main
    if not select_unassigned_variable(assignment):
        return assignment
    else:
        # Each variable is represented by its coordinates in the puzzle
        variable = select_unassigned_variable(assignment)
        # We check each value in a given variable's domain
        for value in order_domain_values():
            # If the value assigned is consistent with assignment given
            # constraints, then add the value to the assignment
            if (is_consistent(assignment, variable, value)):
                assignment[variable[0]][variable[1]] = value
                # print_sudoku(assignment)
                solution = solve_sudoku(assignment)
                # If the solution of the lower recursion call is not
                # failure, then we return the solution. If this is the
                # initial recursive call, then we have found a solution.
                if solution != "FAILURE":
                    return solution
                # If the lower recursive call returned failure, that means
                # that we've reached a "dead-end" even though the current
                # value might not be the one directly causing the conflict.
                # We revert the variable back to empty (a 0).
                assignment[variable[0]][variable[1]] = 0
        # If we reached this point, then none of the values in the
        # variable's domain can satisfy the constraints. We return failure
        # and backtracks If the initial recursive call end up
        # returning failure, then there is no solution to the puzzle).
        return "FAILURE"

# Since this is simple backtracking without any variable ordering, we just
# choose the first empty space that we encounter. This can be improved
# using MRV or degree heuristic. I plan to do this in the bonus. 
def select_unassigned_variable(assignment):
    for row in range(9):
        for col in range(9):
            if assignment[row][col] is 0:
                return [row, col]
    return False 

# Since this is simple backtracking, we assume that the domain of each
# variable contains all possible numbers and only eliminate them during the
# recursive steps. This is inefficient and can be improved using forward
# checking, which will keep track of the domains of each variable and
# update them as assignments are made.
def order_domain_values():
    return [1,2,3,4,5,6,7,8,9]

# Function to check if a given assignment is consistent with the
# constraints 
def is_consistent(assignment, variable, value):
    # Check if the variable is used in the row
    for col in range(9):
        if col != variable[1]:
            if assignment[variable[0]][col] == value:
                return False
    # Check if the variable is used in the column
    for row in range(9):
        if row != variable[0]:
            if assignment[row][variable[1]] == value:
                return False
    # Check if the variable is used in the square
    sq_start_row = variable[0] - variable[0] % 3
    sq_start_col = variable[1] - variable[1] % 3
    for row in range(3):
        for col in range(3):
            if row != variable[0] and col != variable[1]:
                if assignment[sq_start_row + row][sq_start_col + col] == value:
                    return False
    return True

# Checks if the entire puzzle is solved. It simply calls is_consistent on
# every field in the grid
def goal_test(assignment):
    for row in range(9):
        for col in range(9):
            if assignment[row][col] is not 0:
                if is_consistent(assignment, [row, col], assignment[row][col]):
                    return True
    return False

def print_sudoku(grid):
    for row in grid:
        for elem in row:
            print(elem, end = " ")
        print()
    print("\n")
    
def main():
    # Setup parser and parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", 
                        help="Increase verbosity", 
                        action="store_true")
    parser.add_argument("filename",
                        help = "Filename of the sudoku file")    
    args = parser.parse_args()

    # Setup Debugging
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)

    puzzle = [None] * 9

    # Read a sudoku from file
    file = open(args.filename, "r")
    for row in range(9):
        puzzle[row] = list(map(int, file.readline().split(" ")))
    file.close()
    print("Input: ")
    print_sudoku(puzzle)

    # Start timer
    start = timeit.default_timer()
    
    # We first run the goal test to see if the puzzle is already unsolvable
    # with the given numbers (i.e. if there are already duplicates in the
    # rows, cols, or squares)
    if not goal_test(puzzle):
        solution = "FAILURE"
    else:
        solution = solve_sudoku(puzzle)
    
    if solution == "FAILURE":
        print("No solution found")
    else:
        print("Solution:")
        print_sudoku(solution)

    # Stop the timer and print execution time
    stop = timeit.default_timer()
    print("Execution Time:", round(stop - start, 2), "s")  


if __name__ == '__main__':
    main()