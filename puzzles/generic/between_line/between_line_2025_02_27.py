"""PuzzleMadness Between Lines Sudoku — 2025-02-27."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-02-27'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/2/27'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 6, 3, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 4, 0, 2, 7, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 5, 0, 4, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 5, 0, 4, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(5, 1), (4, 1), (5, 2), (6, 3), (7, 2), (8, 3)])
    puzzle.add_between_line([(3, 6), (2, 6), (3, 5), (3, 4), (4, 3)])
    puzzle.add_between_line([(2, 3), (1, 4), (1, 5), (0, 5), (0, 4)])
    puzzle.add_between_line([(3, 2), (3, 3), (2, 2), (1, 2), (2, 1)])
    puzzle.add_between_line([(6, 8), (5, 7), (4, 8), (3, 7)])
    puzzle.add_between_line([(0, 6), (0, 7), (0, 8), (1, 7)])
    puzzle.add_between_line([(0, 2), (1, 1), (0, 0), (1, 0)])
    puzzle.add_between_line([(3, 0), (2, 0), (3, 1), (4, 2)])
    puzzle.add_between_line([(7, 4), (6, 5), (5, 4)])
    puzzle.add_between_line([(7, 0), (8, 0), (8, 1)])
    puzzle.add_between_line([(7, 1), (6, 2), (6, 1)])

    return puzzle
