"""PuzzleMadness Between Lines Sudoku — 2025-09-20."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-09-20'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/9/20'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 3, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 7, 4, 0, 0, 0],
        [0, 0, 0, 0, 6, 0, 7, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 5, 0],
        [0, 7, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 7, 0, 0, 0],
        [1, 0, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 7, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(2, 5), (3, 4), (2, 4), (1, 4), (1, 3), (2, 3)])
    puzzle.add_between_line([(7, 5), (8, 6), (8, 5), (8, 4), (7, 4)])
    puzzle.add_between_line([(6, 0), (5, 1), (4, 1), (3, 1), (4, 0)])
    puzzle.add_between_line([(8, 7), (7, 8), (7, 7), (6, 7), (5, 7)])
    puzzle.add_between_line([(4, 8), (4, 7), (3, 6), (4, 6)])
    puzzle.add_between_line([(0, 5), (1, 5), (0, 6), (1, 6)])
    puzzle.add_between_line([(5, 5), (4, 4), (5, 3), (5, 2)])
    puzzle.add_between_line([(3, 7), (3, 8), (2, 7)])
    puzzle.add_between_line([(0, 2), (0, 1), (1, 0)])
    puzzle.add_between_line([(1, 2), (2, 2), (2, 1)])
    puzzle.add_between_line([(7, 0), (8, 0), (8, 1)])

    return puzzle
