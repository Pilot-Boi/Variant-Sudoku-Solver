"""PuzzleMadness Between Lines Sudoku — 2025-06-30."""

from sudoku.puzzle import SudokuPuzzle


NAME = 'Between Lines Sudoku — 2025-06-30'
SOURCE_URL = 'https://puzzlemadness.co.uk/betweenlinesudoku/hard/2025/6/30'
DIFFICULTY = 'hard'


def create_puzzle():
    grid = [
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [4, 0, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 5, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 8, 7, 0, 0, 0, 3, 0],
        [1, 0, 0, 0, 0, 0, 0, 4, 0],
    ]

    puzzle = SudokuPuzzle(grid)

    puzzle.add_between_line([(2, 0), (3, 1), (2, 2), (1, 3), (0, 3), (1, 2)])
    puzzle.add_between_line([(3, 4), (4, 5), (5, 5), (4, 6), (4, 7)])
    puzzle.add_between_line([(1, 5), (0, 5), (1, 6), (1, 7), (2, 6)])
    puzzle.add_between_line([(3, 8), (3, 7), (3, 6), (2, 5), (2, 4)])
    puzzle.add_between_line([(6, 5), (5, 6), (6, 7), (5, 7)])
    puzzle.add_between_line([(4, 4), (5, 4), (6, 4), (6, 3)])
    puzzle.add_between_line([(3, 3), (3, 2), (4, 3), (5, 2)])
    puzzle.add_between_line([(4, 0), (5, 1), (4, 1)])
    puzzle.add_between_line([(8, 4), (7, 3), (7, 4)])
    puzzle.add_between_line([(0, 2), (1, 1), (0, 1)])

    return puzzle
