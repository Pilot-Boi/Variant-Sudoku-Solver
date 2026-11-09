from sudoku.puzzle import SudokuPuzzle

NAME = "Palindrome Sudoku #001"


def create_puzzle():
    # Zero represents an empty cell.
    grid = [
        [1, 7, 0, 0, 2, 0, 0, 6, 0],
        [2, 6, 0, 0, 4, 0, 7, 3, 1],
        [0, 0, 8, 0, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [3, 2, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 4, 0, 1, 3, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 5, 6, 0, 0],
        [0, 0, 0, 2, 8, 0, 0, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    # Line 1: upper-left, short bend.
    puzzle.add_palindrome([(3, 2), (3, 3), (2, 4)])

    # Line 2: upper-center, bent downward.
    puzzle.add_palindrome([(2, 6), (2, 5), (3, 4), (4, 4)])

    # Line 3: long diagonal on right, ending in a short horizontal segment.
    puzzle.add_palindrome([
        (3, 5), (4, 6), (5, 7), (6, 8), (7, 7), (7, 8)
    ])

    # Line 4: long zigzag from center-left around the lower-left corner.
    puzzle.add_palindrome([
        (4, 3), (5, 3), (4, 2), (5, 1), (5, 0),
        (6, 0), (7, 1), (8, 0), (7, 0)
    ])

    # Line 5: lower-center zigzag.
    puzzle.add_palindrome([
        (6, 1), (7, 2), (6, 3), (6, 4), (7, 3)
    ])

    return puzzle