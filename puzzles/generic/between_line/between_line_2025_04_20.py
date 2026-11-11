"""PuzzleMadness Between Lines Sudoku — 2025-04-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-04-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/4/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [8, 0, 9, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0, 9, 8, 7],
        [0, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 4, 2, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 5, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 2],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(5, 7), (5, 6), (6, 5), (5, 4), (4, 4), (3, 3)])
    puzzle.add_between_line([(4, 6), (5, 5), (4, 5), (3, 6), (2, 6)])
    puzzle.add_between_line([(8, 6), (7, 6), (6, 6), (7, 7), (6, 8)])
    puzzle.add_between_line([(8, 1), (8, 0), (7, 0), (6, 0), (6, 1)])
    puzzle.add_between_line([(1, 6), (0, 7), (1, 7), (1, 8), (0, 8)])
    puzzle.add_between_line([(0, 5), (1, 5), (0, 4), (1, 4)])
    puzzle.add_between_line([(4, 0), (4, 1), (4, 2), (5, 3)])
    puzzle.add_between_line([(3, 4), (2, 3), (1, 3), (2, 2)])
    puzzle.add_between_line([(7, 1), (7, 2), (6, 2)])
    puzzle.add_between_line([(8, 8), (7, 8), (8, 7)])
    puzzle.add_between_line([(8, 3), (7, 4), (7, 3)])
    puzzle.add_between_line([(8, 5), (8, 4), (7, 5)])

    return puzzle
