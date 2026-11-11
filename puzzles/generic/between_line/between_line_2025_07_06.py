"""PuzzleMadness Between Lines Sudoku — 2025-07-06."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-07-06'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/7/6'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 5, 0, 0, 0, 2, 7],
        [0, 0, 1, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 7, 3, 0, 0, 4, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(8, 5), (8, 4), (7, 3), (6, 2), (5, 1), (5, 2)])
    puzzle.add_between_line([(7, 0), (6, 0), (7, 1), (7, 2), (8, 2)])
    puzzle.add_between_line([(4, 1), (4, 0), (3, 1), (2, 2), (1, 2)])
    puzzle.add_between_line([(8, 7), (7, 6), (6, 6), (5, 7), (5, 6)])
    puzzle.add_between_line([(3, 6), (2, 5), (1, 5), (0, 5), (0, 4)])
    puzzle.add_between_line([(4, 8), (3, 7), (2, 7), (2, 8)])
    puzzle.add_between_line([(4, 3), (5, 4), (6, 4), (5, 3)])
    puzzle.add_between_line([(7, 7), (6, 7), (6, 8), (7, 8)])
    puzzle.add_between_line([(4, 4), (5, 5), (4, 6), (4, 5)])
    puzzle.add_between_line([(3, 2), (2, 3), (1, 4)])
    puzzle.add_between_line([(1, 8), (1, 7), (1, 6)])
    puzzle.add_between_line([(0, 1), (1, 1), (2, 1)])

    return puzzle
