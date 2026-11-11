"""PuzzleMadness Between Lines Sudoku — 2025-03-22."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-03-22'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/3/22'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [3, 0, 0, 0, 0, 0, 5, 0, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 8, 0, 9, 5, 0, 0, 4],
        [0, 0, 0, 8, 0, 0, 2, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 7],
        [5, 0, 0, 0, 0, 3, 0, 0, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(2, 0), (1, 0), (1, 1), (0, 2), (1, 2), (2, 3)])
    puzzle.add_between_line([(3, 2), (3, 1), (2, 2), (2, 1), (3, 0)])
    puzzle.add_between_line([(6, 5), (7, 5), (8, 5), (8, 4), (8, 3)])
    puzzle.add_between_line([(4, 3), (3, 4), (4, 5), (5, 6), (4, 6)])
    puzzle.add_between_line([(4, 0), (5, 0), (5, 1), (6, 0), (7, 1)])
    puzzle.add_between_line([(1, 5), (2, 6), (2, 5), (3, 5)])
    puzzle.add_between_line([(5, 3), (6, 2), (7, 3), (6, 3)])
    puzzle.add_between_line([(4, 7), (3, 8), (3, 7), (3, 6)])
    puzzle.add_between_line([(7, 8), (6, 8), (5, 8)])
    puzzle.add_between_line([(2, 8), (2, 7), (1, 8)])
    puzzle.add_between_line([(1, 6), (0, 7), (1, 7)])
    puzzle.add_between_line([(1, 3), (1, 4), (0, 5)])

    return puzzle
