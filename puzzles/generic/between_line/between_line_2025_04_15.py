"""PuzzleMadness Between Lines Sudoku — 2025-04-15."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-04-15'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/4/15'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 1, 0, 0, 0, 0, 0, 0, 6],
        [0, 0, 0, 5, 6, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 0],
        [0, 4, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 4, 0, 5],
        [5, 0, 3, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 5, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(2, 4), (2, 3), (1, 4), (0, 5), (0, 4), (0, 3)])
    puzzle.add_between_line([(5, 8), (4, 8), (5, 7), (5, 6), (6, 5)])
    puzzle.add_between_line([(6, 4), (7, 3), (6, 2), (7, 2), (7, 1)])
    puzzle.add_between_line([(3, 3), (4, 4), (4, 5), (5, 5), (5, 4)])
    puzzle.add_between_line([(2, 5), (2, 6), (2, 7), (1, 7), (1, 8)])
    puzzle.add_between_line([(3, 1), (2, 1), (1, 0), (0, 1)])
    puzzle.add_between_line([(8, 2), (8, 1), (7, 0), (8, 0)])
    puzzle.add_between_line([(6, 0), (5, 1), (5, 0), (4, 0)])
    puzzle.add_between_line([(0, 7), (0, 6), (1, 6)])
    puzzle.add_between_line([(7, 5), (7, 4), (8, 5)])
    puzzle.add_between_line([(6, 7), (7, 6), (7, 7)])

    return puzzle
