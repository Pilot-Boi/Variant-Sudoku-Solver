"""PuzzleMadness Between Lines Sudoku — 2025-06-03."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-06-03'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/6/3'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 7],
        [0, 0, 2, 0, 8, 0, 0, 0, 3],
        [0, 0, 3, 0, 4, 0, 0, 0, 0],
        [6, 0, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 9, 3, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 9, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(8, 3), (8, 2), (7, 2), (6, 3), (7, 4), (7, 3)])
    puzzle.add_between_line([(7, 6), (6, 7), (6, 8), (7, 7), (8, 6)])
    puzzle.add_between_line([(3, 8), (2, 8), (1, 8), (1, 7), (2, 7)])
    puzzle.add_between_line([(3, 6), (2, 5), (1, 6), (1, 5), (0, 5)])
    puzzle.add_between_line([(5, 0), (4, 0), (4, 1), (5, 2)])
    puzzle.add_between_line([(5, 3), (6, 4), (6, 5), (5, 6)])
    puzzle.add_between_line([(1, 0), (2, 1), (3, 0), (2, 0)])
    puzzle.add_between_line([(4, 2), (3, 1), (2, 2)])
    puzzle.add_between_line([(8, 4), (8, 5), (7, 5)])
    puzzle.add_between_line([(7, 0), (7, 1), (6, 1)])
    puzzle.add_between_line([(5, 7), (4, 8), (4, 7)])

    return puzzle
