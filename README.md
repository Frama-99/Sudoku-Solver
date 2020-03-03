# Sudoku Solver

`sudoku.py` takes in a file containing a sudoku puzzle and prints the
solution if one is available, and notifies the user if a solution does not
exist. The script uses a simple backtracking algorithm.

## Running the Script

Run `python sudoku.py [filename]` to run the script on an input file that
contains a sudoku puzzle. The sudoku puzzle file needs to contain 9 lines,
with 9 numbers on each line, delimited by a space. `0` represents an empty
space to be filled out. 

Example:
~~~
0 7 0 0 4 2 0 0 0
0 0 0 0 0 8 6 1 0
3 9 0 0 0 0 0 0 7
0 0 0 0 0 4 0 0 9
0 0 3 0 0 0 7 0 0
5 0 0 1 0 0 0 0 0
8 0 0 0 0 0 0 7 6
0 5 4 8 0 0 0 0 0
0 0 0 6 1 0 0 5 0
~~~

Use `-h` or `--help` to view command line options.

## Structure

The script uses a simple backtracking algorithm. The algorithm is
implemented with a recursive function call with a search that is
depth-first in nature. 

## Future Improvements

Several improvements could be made to make the algorithm more efficient.

### Variable ordering

Currently, we choose the first empty space that we encounter. This can be improved
using MRV or degree heuristic.

### Filtering

Currently, we assume that the domain of each variable contains all possible
numbers and only eliminate them during the recursive steps. This is
inefficient and can be improved using forward checking, which will keep
track of the domains of each variable and update them as assignments are
made.

I plan to do these during the bonus.

## References

- Class slides
- Stackoverflow
- Python documentation pages

## Author

Jiayi (Frank) Ma
