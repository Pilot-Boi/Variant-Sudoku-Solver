"""PuzzleMadness Between Lines Sudoku — 2025-03-01."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-03-01'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/3/1'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [5, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 6, 0, 0, 3, 0, 0, 0, 7],
        [0, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 5, 0, 1],
        [8, 0, 0, 0, 2, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(6, 3), (5, 4), (5, 5), (6, 5), (6, 6), (7, 5)])
    puzzle.add_between_line([(6, 8), (5, 7), (5, 8), (4, 8), (3, 8)])
    puzzle.add_between_line([(3, 6), (2, 7), (1, 7), (0, 8), (1, 8)])
    puzzle.add_between_line([(1, 4), (2, 4), (3, 5), (2, 5), (1, 6)])
    puzzle.add_between_line([(7, 1), (6, 1), (5, 2), (5, 1)])
    puzzle.add_between_line([(6, 2), (5, 3), (4, 4), (4, 5)])
    puzzle.add_between_line([(7, 0), (8, 0), (8, 1), (7, 2)])
    puzzle.add_between_line([(6, 7), (7, 6), (7, 7), (7, 8)])
    puzzle.add_between_line([(4, 3), (4, 2), (3, 1)])
    puzzle.add_between_line([(4, 0), (3, 0), (2, 0)])
    puzzle.add_between_line([(3, 7), (4, 6), (4, 7)])
    puzzle.add_between_line([(0, 3), (0, 2), (1, 1)])

    return puzzle
